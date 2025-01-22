

class TestRetriver:
    def test_search(
            self,
            query: str,
            k: int=3,
            expand_to_n_quries: int = 3
    ) -> list:
        query_model = Query.from_str(query)