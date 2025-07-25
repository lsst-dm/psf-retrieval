"""Models for psf-retrieval."""

from pydantic import BaseModel, Field
from safir.metadata import Metadata as SafirMetadata
from safir.uws import ParametersModel
from vo_models.uws import MultiValuedParameter, Parameter, Parameters

from .domain import WorkerPsfRetrievalParameters

__all__ = ["Index", "PsfRetrievalParameters", "PsfRetrievalXmlParameters"]


class Index(BaseModel):
    """Metadata returned by the external root URL of the application.

    Notes
    -----
    As written, this is not very useful. Add additional metadata that will be
    helpful for a user exploring the application, or replace this model with
    some other model that makes more sense to return from the application API
    root.
    """

    metadata: SafirMetadata = Field(..., title="Package metadata")


class PsfRetrievalXmlParameters(Parameters):
    """XML representation of job parameters.

    Add fields here for all the input parameters to the job in the format
    suitable for the IVOA UWS standard (key/value parameters). If a key can be
    repeated, use ``MultiValuedParameter`` as its type. Otherwise, use
    ``Parameter``.
    """

    id: MultiValuedParameter
    ra: MultiValuedParameter = Field(
        [], description="One or more RA values (deg)"
    )
    dec: MultiValuedParameter = Field(
        [], description="One or more Dec values (deg)"
    )


class PsfRetrievalParameters(
    ParametersModel[WorkerPsfRetrievalParameters, PsfRetrievalXmlParameters]
):
    """Model for job parameters.

    Add fields here for all the input parameters to a job, and then update
    ``to_worker_parameters`` and ``to_xml_model`` to do the appropriate
    conversions.
    """

    id: str = Field(
        ..., title="Dataset ID", description="Identifier of the PSF dataset"
    )
    ra: float = Field(
        ...,
        title="Right Ascension",
        description="ICRS right ascension in decimal degrees",
    )
    dec: float = Field(
        ...,
        title="Declination",
        description="ICRS declination in decimal degrees",
    )

    def to_worker_parameters(self) -> WorkerPsfRetrievalParameters:
        """Convert to the worker (domain) model."""
        return WorkerPsfRetrievalParameters(
            dataset_id=self.id,
            ra=self.ra,
            dec=self.dec,
        )

    def to_xml_model(self) -> PsfRetrievalXmlParameters:
        """Convert to the flat XML model for IVOA UWS."""
        return PsfRetrievalXmlParameters(
            id=[Parameter(id="id", value=self.id)],
            ra=[Parameter(id="ra", value=str(self.ra))],
            dec=[Parameter(id="dec", value=str(self.dec))],
        )
