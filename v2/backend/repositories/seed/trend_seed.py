from backend.models.trend_model import Trend


def get_seed_trends() -> list[Trend]:
    return [
        Trend(id="t1", category="Technology", topic="#OpenSource", post_count=18400),
        Trend(id="t2", category="Sports", topic="Champions League", post_count=52100),
        Trend(id="t3", category="Business & Finance", topic="Interest Rates", post_count=9800),
        Trend(id="t4", category="Entertainment", topic="#SeasonFinale", post_count=27600),
        Trend(id="t5", category="Technology", topic="AI Agents", post_count=41200),
        Trend(id="t6", category="Politics", topic="Election Results", post_count=63500),
        Trend(id="t7", category="Science", topic="Mars Rover", post_count=7200),
    ]
