from src.domain.chunks import Chunk
from src.domain.embedded_chunks import EmbeddedChunk

def _add_chunks_metadata(chunks: list[Chunk], metadata: dict) -> dict:
    for chunk in chunks:
        category = chunk.get_category()
        if category not in metadata:
            metadata[category] = chunk.metadata
        if "authors" not in metadata[category]:
            metadata[category]["authors"] = list()

        metadata[category]["num_chunks"] = metadata[category].get("num_chunks", 0) + 1
        metadata[category]["authors"].append(chunk.author_full_name)

    for value in metadata.values():
        if isinstance(value, dict) and "authors" in value:
            value["authors"] = list(set(value["authors"]))

    return metadata


def _add_embeddings_metadata(embedded_chunks: list[EmbeddedChunk], metadata: dict) -> dict:
    for embedded_chunk in embedded_chunks:
        category = embedded_chunk.get_category()
        if category not in metadata:
            metadata[category] = embedded_chunk.metadata
        if "authors" not in metadata[category]:
            metadata[category]["authors"] = list()

        metadata[category]["authors"].append(embedded_chunk.author_full_name)

    for value in metadata.values():
        if isinstance(value, dict) and "authors" in value:
            value["authors"] = list(set(value["authors"]))

    return metadata