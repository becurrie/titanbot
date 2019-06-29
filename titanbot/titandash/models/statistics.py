from django.db import models
from django.urls import reverse

from titandash.constants import DATETIME_FMT
from titandash.bot.core.maps import ARTIFACT_TIER_MAP
from titandash.bot.core.utilities import convert


GAME_STATISTICS_HELP_TEXT = {
    "highest_stage_reached": "Highest stage reached in game overall.",
    "total_pet_level": "Total pet level reached in game overall.",
    "gold_earned": "How much gold has been earned in game overall.",
    "taps": "How many taps have taken place in game overall.",
    "titans_killed": "How many titans have been killed in game overall.",
    "bosses_killed": "How many bosses have been killed in game overall.",
    "critical_hits": "How many critical hits have been scored in game overall.",
    "chestersons_killed": "How many chestersons have been killed in game overall.",
    "prestiges": "How many total prestiges have taken place in game overall.",
    "play_time": "How much active play time has been accrued in game overall.",
    "relics_earned": "How many relics have been earned game overall.",
    "fairies_tapped": "How many fairies have been tapped on in game overall.",
    "daily_achievements": "How many daily achievements have been completed in game overall."
}


class GameStatistics(models.Model):
    """
    GameStatistics Model.

    Represents all in game statistics that can be grabbed by the Bot. An OCR check is performed on the in game stats.
    These values are updated when these stats are pushed from the Bot, to the database.
    """
    class Meta:
        verbose_name = "Game Statistics"
        verbose_name_plural = "Game Statistics"

    highest_stage_reached = models.CharField(verbose_name="Highest Stage Reached", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["highest_stage_reached"])
    total_pet_level = models.CharField(verbose_name="Total Pet Level", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["total_pet_level"])
    gold_earned = models.CharField(verbose_name="Gold Earned", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["gold_earned"])
    taps = models.CharField(verbose_name="Taps", max_length=255, blank=True, null=True, help_text=GAME_STATISTICS_HELP_TEXT["taps"])
    titans_killed = models.CharField(verbose_name="Titans Killed", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["titans_killed"])
    bosses_killed = models.CharField(verbose_name="Bosses Killed", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["bosses_killed"])
    critical_hits = models.CharField(verbose_name="Critical Hits", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["critical_hits"])
    chestersons_killed = models.CharField(verbose_name="Chestersons Killed", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["chestersons_killed"])
    prestiges = models.CharField(verbose_name="Prestiges", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["prestiges"])
    play_time = models.CharField(verbose_name="Play Time", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["play_time"])
    relics_earned = models.CharField(verbose_name="Relics Earned", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["relics_earned"])
    fairies_tapped = models.CharField(verbose_name="Fairies Tapped", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["fairies_tapped"])
    daily_achievements = models.CharField(verbose_name="Daily Achievements", blank=True, null=True, max_length=255, help_text=GAME_STATISTICS_HELP_TEXT["daily_achievements"])

    def __str__(self):
        return "GameStatistics".format(key=self.pk)

    def highest_stage(self):
        if self.highest_stage_reached is not None and self.highest_stage_reached != "":
            return convert(self.highest_stage_reached)
        else:
            return None

    def json(self):
        return {
            "highest_stage_reached": self.highest_stage_reached,
            "total_pet_level": self.total_pet_level,
            "gold_earned": self.gold_earned,
            "taps": self.taps,
            "titans_killed": self.titans_killed,
            "bosses_killed": self.bosses_killed,
            "critical_hits": self.critical_hits,
            "chestersons_killed": self.chestersons_killed,
            "prestiges": self.prestiges,
            "play_time": self.play_time,
            "relics_earned": self.relics_earned,
            "fairies_tapped": self.fairies_tapped,
            "daily_achievements": self.daily_achievements
        }


BOT_STATISTICS_HELP_TEXT = {
    "premium_ads": "How many premium ads have been earned and tracked by the bot.",
    "actions": "How many sets of actions have been ran by the bot.",
    "updates": "How many times has bot statistics been updated."
}


class BotStatistics(models.Model):
    """
    BotStatistics Model.

    Bot statistics taken from the Bot while running and executing functions.
    """
    class Meta:
        verbose_name = "Bot Statistics"
        verbose_name_plural = "Bot Statistics"

    premium_ads = models.PositiveIntegerField(verbose_name="Premium Ads", default=0, help_text=BOT_STATISTICS_HELP_TEXT["premium_ads"])
    actions = models.PositiveIntegerField(verbose_name="Actions", default=0, help_text=BOT_STATISTICS_HELP_TEXT["actions"])
    updates = models.PositiveIntegerField(verbose_name="Updates", default=0, help_text=BOT_STATISTICS_HELP_TEXT["updates"])

    def __str__(self):
        return "BotStatistics".format(key=self.pk)

    def json(self):
        return {
            "premium_ads": self.premium_ads,
            "actions": self.actions,
            "updates": self.updates
        }


ARTIFACT_OWNED_HELP_TEXT = {
    "artifact": "Specify the artifact being used.",
    "owned": "Specify if this artifact is owned or not."
}


class ArtifactOwned(models.Model):
    """
    ArtifactOwned Model.

    Artifacts can be associated to a boolean representing whether or not they are currently owned.
    """
    class Meta:
        verbose_name = "Artifact Owned"
        verbose_name_plural = "Artifacts Owned"

    artifact = models.ForeignKey(verbose_name="Artifact", to="Artifact", on_delete=models.CASCADE, help_text=ARTIFACT_OWNED_HELP_TEXT["artifact"])
    owned = models.BooleanField(verbose_name="Owned", default=False, help_text=ARTIFACT_OWNED_HELP_TEXT["owned"])

    def __str__(self):
        return "{artifact} ({owned})".format(artifact=self.artifact, owned=self.owned)

    def json(self):
        """Return ArtifactOwned as JSON Compliant Object."""
        art = self.artifact.json()
        art.update({"owned": self.owned})

        return art


class ArtifactStatisticsManager(models.Manager):
    def grab(self):
        """
        Attempt to grab the current ArtifactStatistics instance. One will be generated with some default values
        if one does not already exist.
        """
        from .artifact import Artifact, Tier

        if len(self.all()) == 0:
            arts = self.create()
        else:
            arts = self.all().first()

        for tier, dct in ARTIFACT_TIER_MAP.items():
            for key, value in dct.items():
                if key not in arts.artifacts.all().values_list("artifact__name", flat=True):
                    arts.artifacts.add(ArtifactOwned.objects.create(
                        artifact=Artifact.objects.get_or_create(
                            name=key,
                            tier=Tier.objects.get_or_create(tier=tier, name="Tier {tier}".format(tier=tier))[0],
                            key=value[1],
                            image="{name}.png".format(name=key.replace("'", ""))
                        )[0]))

        return arts


ARTIFACT_STATISTICS_HELP_TEXT = {
    "artifacts": "Choose the artifacts associated with this artifact statistics instance."
}


class ArtifactStatistics(models.Model):
    """
    ArtifactStatistics Model.

    Artifact statistics stores the relation between artifacts and whether or not they're owned
    into a single artifact statistics instance.
    """
    class Meta:
        verbose_name = "Artifact Statistics"
        verbose_name_plural = "Artifact Statistics"

    objects = ArtifactStatisticsManager()
    artifacts = models.ManyToManyField(verbose_name="Artifacts", to="ArtifactOwned", help_text=ARTIFACT_STATISTICS_HELP_TEXT["artifacts"])

    def owned(self):
        return self.artifacts.filter(owned=True)

    def missing(self):
        return self.artifacts.filter(owned=False)

    def __str__(self):
        return "ArtifactStatistics ({owned}/{all})".format(owned=len(self.owned()), all=len(self.artifacts.all()))


SESSION_HELP_TEXT = {
    "uuid": "Specify the unique identifier for this session.",
    "version": "Specify the version of the bot during this session.",
    "start": "Start datetime for this session.",
    "end": "End datetime for this session.",
    "log": "Specify the file path to the log file associated with this session.",
    "game_statistic_differences": "Game statistic differences associated with session.",
    "bot_statistic_differences": "Bot statistic differences associated with session.",
    "configuration": "Config instance associated with this session."
}


class Log(models.Model):
    """
    Log Model.

    Store references to log files generated so that they can be retrieved through the dashboard if needed.
    """
    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    log_file = models.CharField(verbose_name="Log File", max_length=255)

    def json(self):
        ctx = {
            "id": self.pk,
            "filename": self.log_file,
            "data": []
        }

        with open(self.log_file) as file:
            lines = file.readlines()
            for index, line in enumerate(lines, start=1):
                ctx["data"].append({
                    "num": index,
                    "line": line
                })

        return ctx


class Session(models.Model):
    """
    Session Model.

    Sessions are started each time the Bot is started. A session is identified by it's unique identifier
    that is generated by the Bot when started. It stores information about the differences between stats
    from when the Bot was started, and whenever the last statistic update took place. The configuration used
    is also stored here which can be used for debugging purposes or error auditing.
    """
    class Meta:
        verbose_name = "Session"
        verbose_name_plural = "Sessions"

    uuid = models.CharField(verbose_name="Unique Identifier", blank=True, null=True, max_length=255, help_text=SESSION_HELP_TEXT["uuid"])
    version = models.CharField(verbose_name="Version", blank=True, null=True, max_length=255, help_text=SESSION_HELP_TEXT["version"])
    start = models.DateTimeField(verbose_name="Start Date", blank=True, null=True, help_text=SESSION_HELP_TEXT["start"])
    end = models.DateTimeField(verbose_name="End Date", blank=True, null=True, help_text=SESSION_HELP_TEXT["end"])
    log = models.ForeignKey(verbose_name="Log File", to="Log", on_delete=models.CASCADE, blank=True, null=True, max_length=255, help_text=SESSION_HELP_TEXT["log"])
    configuration = models.ForeignKey(verbose_name="Configuration", to="Configuration", on_delete=models.CASCADE, blank=True, null=True, help_text=SESSION_HELP_TEXT["configuration"])

    def __str__(self):
        return "Session [{uuid}] v{version}".format(uuid=self.uuid, version=self.version)

    def duration(self):
        if not self.start or not self.end:
            return "N/A"

        s = (self.end - self.start).total_seconds()
        hours = s // 3600
        s = s - (hours * 3600)
        minutes = s // 60
        seconds = s - (minutes * 60)

        return "{:02}:{:02}:{:02}".format(int(hours), int(minutes), int(seconds))

    def json(self):
        """Return Session and Associated Models As JSON Compliant Dictionary."""
        from titandash.models.prestige import Prestige
        dct = {
            "uuid": self.uuid,
            "version": self.version,
            "start": {
                "datetime": str(self.start),
                "formatted": self.start.astimezone().strftime(DATETIME_FMT) if self.start else "N/A",
                "epoch": int(self.start.astimezone().timestamp()) if self.start else 0
            },
            "end": {
                "datetime": str(self.end),
                "formatted": self.end.astimezone().strftime(DATETIME_FMT) if self.end else "N/A",
                "epoch": int(self.end.astimezone().timestamp()) if self.end else 0
            },
            "log": reverse('log', kwargs={'pk': self.log.pk}) if self.log else "N/A",
            "duration": str(self.duration()),
        }

        prestiges = Prestige.objects.filter(session=self)
        if len(prestiges) > 0:
            prestiges = [p.json() for p in prestiges]
            count = len(prestiges)
        else:
            prestiges = []
            count = 0

        dct["prestiges"] = {
            "prestiges": prestiges,
            "count": count
        }

        return dct


STATS_HELP_TEXT = {
    "game_statistics": "Game Statistics associated with this statistics instance.",
    "bot_statistics": "Bot Statistics associated with this statistics instance.",
    "sessions": "Sessions associated with this statistics instance."
}


class StatisticsManager(models.Manager):
    def grab(self):
        """
        Attempt to grab the current Statistics instance. One will be generated with some default values
        if one does not already exist.
        """
        if len(self.all()) == 0:
            game_statistics = GameStatistics.objects.create()
            bot_statistics = BotStatistics.objects.create()
            self.create(game_statistics=game_statistics, bot_statistics=bot_statistics)

        # Returning the existing instance.
        return self.all().first()


class Statistics(models.Model):
    """
    Statistics Model.

    The statistics model is used to contain all statistics in one single location.
    """
    class Meta:
        verbose_name = "Statistics"
        verbose_name_plural = "Statistics"

    objects = StatisticsManager()
    game_statistics = models.ForeignKey(verbose_name="Game Statistics", to="GameStatistics", on_delete=models.CASCADE, blank=True, null=True, help_text=STATS_HELP_TEXT["game_statistics"])
    bot_statistics = models.ForeignKey(verbose_name="Bot Statistics", to="BotStatistics", on_delete=models.CASCADE, blank=True, null=True, help_text=STATS_HELP_TEXT["bot_statistics"])
    sessions = models.ManyToManyField(verbose_name="Sessions", to="Session", blank=True, help_text=STATS_HELP_TEXT["sessions"])

    def __str__(self):
        return "Statistics ({key})".format(key=self.pk)


class PrestigeStatisticsManager(models.Manager):
    def grab(self):
        """
        Attempt to grab the current PrestigeStatistics instance. One will be generated with some default values
        if one does not already exist.
        """
        if len(self.all()) == 0:
            self.create()

        # Returning the existing instance.
        return self.all().first()


PRESTIGE_STATISTICS_HELP_TEXT = {
    "prestiges": "Choose the prestiges that are associated with this prestige statistics instance."
}


class PrestigeStatistics(models.Model):
    """
    PrestigeStatistics Model.

    Store all statistics related to prestiges that take place in game.
    """
    class Meta:
        verbose_name = "Prestige Statistics"
        verbose_name_plural = "Prestige Statistics"

    objects = PrestigeStatisticsManager()
    prestiges = models.ManyToManyField(verbose_name="Prestiges", to="Prestige", blank=True, help_text=PRESTIGE_STATISTICS_HELP_TEXT["prestiges"])

    def __str__(self):
        return "PrestigeStatistics [{count} Prestiges]".format(count=self.prestiges.all().count(), key=self.pk)
