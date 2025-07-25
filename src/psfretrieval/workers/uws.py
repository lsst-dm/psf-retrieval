"""Worker for UWS database updates."""

from __future__ import annotations

import structlog
from safir.logging import configure_logging

from ..config import config, uws

__all__ = ["WorkerSettings"]

# Match the main app logging profile.
configure_logging(
    name="psfretrieval", profile=config.profile, log_level=config.log_level
)

# Build the ARQ background worker that processes jobs and updates UWS state.
WorkerSettings = uws.build_worker(structlog.get_logger("psfretrieval"))
"""arq configuration for the UWS database worker."""
