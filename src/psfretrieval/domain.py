"""Domain models for psf-retrieval."""

from __future__ import annotations

from pydantic import BaseModel, Field

__all__ = [
    "WorkerPsfRetrievalParameters",
]


class WorkerPsfRetrievalParameters(BaseModel):
    """Parameters passed to the PSF retrieval backend task."""

    dataset_id: str = Field(
        ...,
        title="Dataset ID",
        description="Unique identifier for the PSF dataset to retrieve",
    )
    ra: float = Field(
        ...,
        title="Right Ascension (deg)",
        description="ICRS right ascension in decimal degrees",
    )
    dec: float = Field(
        ...,
        title="Declination (deg)",
        description="ICRS declination in decimal degrees",
    )
