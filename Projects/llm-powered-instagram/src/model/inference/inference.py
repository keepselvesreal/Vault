from typing import Optional, Dict, Any
import json

from loguru import logger
# from unsloth import FastLanguageModel, is_bf16_supported
try:
    import boto3
except ModuleNotFoundError:
    logger.warning("Couldn't load AWS or SageMaker imports. Run 'poetry install --with aws' to support AWS.")
from transformers import (
    AutoModelForCausalLM,
    AutoTokenizer,
)


from src.domain.inference import Inference
from src.settings import settings

# class LLMLocalInference(Inference):
#     def __init__(
#             self,
#             model_name: str = "meta-llama/Llama-3.1-8B", 
#             default_payload: Optional[Dict[str, Any]] = None,
#             Inference_component_name: Optional[str] = None,
#     ) -> None:
#         super().__init__()
#         self.model = FastLanguageModel.from_pretrained(model_name=model_name)
#         self.payload = default_payload if default_payload else self._default_payload()
#         self.inference_component_name = Inference_component_name

#     def _default_payload(self) -> Dict[str, Any]:
#         return {
#             "inputs": "what's your role?",
#             "parameters": {
#                 "max_new_tokens": 150 ,# settings.MAX_NEW_TOKENS_INFERENCE,
#                 "top_p": 0.9, # settings.TOP_P_INFERENCE,
#                 "teperature": 0.01, # settings.TEMPERATURE_INFERENCE,
#                 "return_full_text": False,
#             },
#         }
    
#     def set_payload(self, inputs:str, parameters: Optional[Dict[str, Any]] = None) -> None:
#         self.payload["inputs"] = inputs
#         if parameters:
#             self.payload["parameters"] = parameters

#     def inference(self) -> Dict[str, Any]:
#         try:
#             logger.info("Inference request sent.")
#             model = FastLanguageModel.for_inference(self.model)
#             model.generate()

#         except Exception:
#             logger.exception("Local inference failed.")

#             raise


class PlatformAgnosticInference(Inference):
    def __init__(
            self,
            model_path: str,
            default_payload: Optional[Dict[str, Any]] = None, 
            ):
        # self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model = AutoModelForCausalLM.from_pretrained(
            model_path,
            token=settings.HUGGINGFACE_ACCESS_TOKEN,
        ).to(self.device) # TODO pytorch 설치해야
        self.tokenizer = AutoTokenizer.from_pretrained(
            model_path,
            token=settings.HUGGINGFACE_ACCESS_TOKEN,
        )
        self.payload = default_payload if default_payload else self._default_payload()
    def _default_payload(self) -> Dict[str, Any]:
        return {
            "inputs": "How is the weather?",
            "parameters": {
                "max_new_tokens": settings.MAX_NEW_TOKENS_INFERENCE,
                "top_p": settings.TOP_P_INFERENCE,
                "temperature": settings.TEMPERATURE_INFERENCE,
                "return_full_text": False, # TODO 사용 가능한 파라미터인지 확인 필요
            },
        }


    def set_payload(self, inputs: str, parameters: Optional[Dict[str, Any]] = None) -> None:
        inputs = self.tokenizer([inputs],  return_tensors="pt").to(self.device) # TODO self.device 확실히 처리되어야 함
        self.payload["inputs"] = inputs
        if parameters:
            self.payload["parameters"].update(parameters)

    def inference(self):
        inputs = self.payload["inputs"]
        parameters = self.payload["parameters"]
        output = self.model.generate(**inputs, **parameters)
        generated_text = self.tokenizer.decode(output[0], skip_special_tokens=True)
        requested_format_answer = [{"generated_text": generated_text}]
        
        return requested_format_answer


class LLMInferenceSagemakerEndpoint(Inference):
    def __init__(
        self,
        endpoint_name: str,
        default_payload: Optional[Dict[str, Any]] = None,
        inference_component_name: Optional[str] = None,
    ) -> None:
        super().__init__()

        self.client = boto3.client(
            "sagemaker-runtime",
            region_name=settings.AWS_REGION,
            aws_access_key_id=settings.AWS_ACCESS_KEY,
            aws_secret_access_key=settings.AWS_SECRET_KEY,
        )
        self.endpoint_name = endpoint_name
        self.payload = default_payload if default_payload else self._default_payload()
        self.inference_component_name = inference_component_name

    def _default_payload(self) -> Dict[str, Any]:
        """
        Generates the default payload for the inference request.

        Returns:
            dict: The default payload.
        """

        return {
            "inputs": "How is the weather?",
            "parameters": {
                "max_new_tokens": settings.MAX_NEW_TOKENS_INFERENCE,
                "top_p": settings.TOP_P_INFERENCE,
                "temperature": settings.TEMPERATURE_INFERENCE,
                "return_full_text": False,
            },
        }

    def set_payload(self, inputs: str, parameters: Optional[Dict[str, Any]] = None) -> None:
        """
        Sets the payload for the inference request.

        Args:
            inputs (str): The input text for the inference.
            parameters (dict, optional): Additional parameters for the inference. Defaults to None.
        """

        self.payload["inputs"] = inputs
        if parameters:
            self.payload["parameters"].update(parameters)

    def inference(self) -> Dict[str, Any]:
        """
        Performs the inference request using the SageMaker endpoint.

        Returns:
            dict: The response from the inference request.
        Raises:
            Exception: If an error occurs during the inference request.
        """

        try:
            logger.info("Inference request sent.")
            invoke_args = {
                "EndpointName": self.endpoint_name,
                "ContentType": "application/json",
                "Body": json.dumps(self.payload),
            }
            if self.inference_component_name not in ["None", None]:
                invoke_args["InferenceComponentName"] = self.inference_component_name
            response = self.client.invoke_endpoint(**invoke_args)
            response_body = response["Body"].read().decode("utf8")

            return json.loads(response_body)

        except Exception:
            logger.exception("SageMaker inference failed.")

            raise