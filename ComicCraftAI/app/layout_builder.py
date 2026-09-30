from .models import Panel


def build_comic_layout(
    outline,
    story
):

    story_by_number = {
        panel["panel_number"]: panel
        for panel in story.get(
            "panels",
            []
        )
    }

    layout = []

    for item in outline.get(
        "panels",
        []
    ):

        number = item[
            "panel_number"
        ]

        story_data = story_by_number.get(
            number,
            {}
        )

        panel = Panel(

            panel_number=number,

            title=item.get(
                "title",
                f"Panel {number}"
            ),

            scene_description=item.get(
                "scene_description",
                ""
            ),

            image_prompt=item.get(
                "image_prompt",
                ""
            ),

            caption=story_data.get(
                "caption",
                ""
            ),

            narration=story_data.get(
                "narration",
                ""
            ),

            dialogue=story_data.get(
                "dialogue",
                ""
            )
        )

        layout.append(panel)

    return layout