"""Domain models for psf-retrieval."""

from __future__ import annotations

from pydantic import BaseModel

__all__ = ["WorkerPsfretrievalModel"]


class WorkerPsfretrievalModel(BaseModel):
    """Parameter model for backend workers.

    Add fields here for all the parameters passed to backend jobs.
    """
