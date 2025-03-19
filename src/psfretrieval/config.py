"""Configuration definition."""

from __future__ import annotations

from pydantic import Field, SecretStr
from pydantic_settings import SettingsConfigDict
from safir.logging import LogLevel, Profile
from safir.uws import UWSApplication, UWSAppSettings, UWSConfig, UWSRoute
from vo_models.uws import JobSummary

from .dependencies import post_params_dependency
from .models import PsfretrievalParameters, PsfretrievalXmlParameters

__all__ = ["Config", "config"]


class Config(UWSAppSettings):
    """Configuration for psf-retrieval."""

    model_config = SettingsConfigDict(
        env_prefix="PSF_RETRIEVAL_", case_sensitive=False
    )

    log_level: LogLevel = Field(
        LogLevel.INFO, title="Log level of the application's logger"
    )

    name: str = Field("psf-retrieval", title="Name of application")

    path_prefix: str = Field(
        "/psf-retrieval", title="URL prefix for application"
    )

    profile: Profile = Field(
        Profile.development, title="Application logging profile"
    )

    slack_webhook: SecretStr | None = Field(
        None,
        title="Slack webhook for alerts",
        description="If set, alerts will be posted to this Slack webhook",
    )

    @property
    def uws_config(self) -> UWSConfig:
        """Corresponding configuration for the UWS subsystem."""
        return self.build_uws_config(
            job_summary_type=JobSummary[PsfretrievalXmlParameters],
            parameters_type=PsfretrievalParameters,
            worker="psf_retrieval",
            async_post_route=UWSRoute(
                dependency=post_params_dependency,
                summary="Create async psf-retrieval job",
                description="Create a new UWS job for psf-retrieval",
            ),
        )


config = Config()
"""Configuration for psf-retrieval."""

uws = UWSApplication(config.uws_config)
"""The UWS application for this service."""
