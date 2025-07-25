"""Job parameter dependencies."""

from typing import Annotated

from fastapi import Form, Query

from .models import PsfRetrievalParameters

__all__ = [
    "post_params_dependency",
]


async def post_params_dependency(
    *,
    # Add POST parameters here. All of them should be Form() parameters.
    # Use str | None for single-valued attributes and list[str] | None for
    # parameters that can be given more than one time.
    id: Annotated[
        str,
        Form(..., title="Dataset ID", description="PSF dataset identifier"),
    ],
    ra: Annotated[
        float, Form(..., title="RA (deg)", description="Right ascension")
    ],
    dec: Annotated[
        float, Form(..., title="Dec (deg)", description="Declination")
    ],
) -> PsfRetrievalParameters:
    """Parse POST parameters into job parameters for a PSF retrieval."""
    return PsfRetrievalParameters(id=id, ra=ra, dec=dec)


async def get_params_dependency(
    *,
    id: Annotated[
        str,
        Query(..., title="Dataset ID", description="PSF dataset identifier"),
    ],
    ra: Annotated[
        float, Query(..., title="RA (deg)", description="Right ascension")
    ],
    dec: Annotated[
        float, Query(..., title="Dec (deg)", description="Declination")
    ],
) -> PsfRetrievalParameters:
    """Parse GET parameters into job parameters for a PSF retrieval."""
    return PsfRetrievalParameters(id=id, ra=ra, dec=dec)
