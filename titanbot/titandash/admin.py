from django.contrib import admin
from django.contrib.admin.decorators import register
from django.contrib.auth.models import User, Group

# from .models.token import Token
from .models.artifact import Artifact, Tier
from .models.configuration import Configuration
from .models.bot import BotInstance
from .models.prestige import Prestige
from .models.queue import Queue
from .models.statistics import (
    Statistics, GameStatistics, BotStatistics, ArtifactOwned, ArtifactStatistics,
    PrestigeStatistics, Session
)


# @register(Token)
# class TokenAdmin(admin.ModelAdmin):
#     list_display = ["__str__"]
#
#
# @register(BotInstance)
# class BotInstanceAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "state", "started", "session"]
#
#
# @register(Prestige)
# class PrestigeAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "timestamp", "stage", "time"]
#
#
# @register(Queue)
# class QueueAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "created"]
#
#
# @register(Tier)
# class TierAdmin(admin.ModelAdmin):
#     pass
#
#
# @register(Artifact)
# class ArtifactAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "name", "tier", "key", "image"]


@register(Configuration)
class ConfigurationAdmin(admin.ModelAdmin):
    filter_horizontal = ["upgrade_owned_tier", "ignore_artifacts", "upgrade_artifacts"]
    fieldsets = (
        (None, {
            "classes": ("expanded",),
            "fields": ("name",),
        }),
        ("Runtime Settings", {
            "classes": ("expanded",),
            "fields": ("soft_shutdown_on_critical_error", "soft_shutdown_update_stats", "post_action_min_wait_time",
                       "post_action_max_wait_time"),
        }),
        ("Device Settings", {
            "classes": ("expanded",),
            "fields": ("emulator",),
        }),
        ("Generic Settings", {
            "classes": ("expanded",),
            "fields": ("enable_premium_ad_collect", "enable_egg_collection", "enable_tapping", "enable_tournaments",),
        }),
        ("Daily Achievement Settings", {
            "classes": ("expanded",),
            "fields": ("enable_daily_achievements", "daily_achievements_check_on_start", "daily_achievements_check_every_x_hours",),
        }),
        ("General Action Settings", {
            "classes": ("expanded",),
            "fields": ("run_actions_every_x_seconds", "run_actions_on_start", "order_level_heroes", "order_level_master", "order_level_skills",),
        }),
        ("Master Action Settings", {
            "classes": ("expanded",),
            "fields": ("enable_master", "master_level_intensity",),
        }),
        ("Heroes Action Settings", {
            "classes": ("expanded",),
            "fields": ("enable_heroes", "hero_level_intensity",),
        }),
        ("Skills Action Settings", {
            "classes": ("expanded",),
            "fields": ("enable_skills", "activate_skills_on_start", "interval_heavenly_strike", "interval_deadly_strike",
                       "interval_hand_of_midas", "interval_fire_sword", "interval_war_cry", "interval_shadow_clone",
                       "force_enabled_skills_wait", "max_skill_if_possible", "skill_level_intensity"),
        }),
        ("Prestige Action Settings", {
            "classes": ("expanded",),
            "fields": ("enable_auto_prestige", "prestige_x_minutes", "prestige_at_stage", "prestige_at_max_stage",
                       "prestige_at_max_stage_percent",),
        }),
        ("Artifacts Action Settings", {
            "classes": ("expanded",),
            "fields": ("enable_artifact_purchase", "upgrade_owned_artifacts", "upgrade_owned_tier", "shuffle_artifacts",
                       "ignore_artifacts", "upgrade_artifacts",),
        }),
        ("Stats Settings", {
            "classes": ("expanded",),
            "fields": ("enable_stats", "update_stats_on_start", "update_stats_every_x_minutes",),
        }),
        ("Artifact Parsing Settings", {
            "classes": ("expanded",),
            "fields": ("bottom_artifact",),
        }),
        ("Recovery Settings", {
            "classes": ("expanded",),
            "fields": ("recovery_check_interval_minutes", "recovery_allowed_failures",),
        }),
        ("Logging Settings", {
            "classes": ("expanded",),
            "fields": ("enable_logging", "logging_level",),
        }),
    )


admin.site.unregister(User)
admin.site.unregister(Group)


# @register(Statistics)
# class StatisticsAdmin(admin.ModelAdmin):
#     filter_horizontal = ["sessions"]
#
#
# @register(GameStatistics)
# class GameStatisticsAdmin(admin.ModelAdmin):
#     pass
#
#
# @register(BotStatistics)
# class BotStatisticsAdmin(admin.ModelAdmin):
#     pass
#
#
# @register(ArtifactStatistics)
# class ArtifactStatisticsAdmin(admin.ModelAdmin):
#     filter_horizontal = ["artifacts"]
#     pass
#
#
# @register(ArtifactOwned)
# class ArtifactOwnedAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "owned"]
#
#
# @register(PrestigeStatistics)
# class PrestigeStatisticsAdmin(admin.ModelAdmin):
#     pass
#
#
# @register(Session)
# class SessionAdmin(admin.ModelAdmin):
#     list_display = ["__str__", "uuid", "version", "start"]
#     pass
