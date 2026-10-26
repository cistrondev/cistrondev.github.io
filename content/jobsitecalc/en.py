# Jobsite Calc in English. build.py reads the dict L below.
#
# Same keys as content/unfollowers/en.py: name, path, og_locale, ui (frame words
# that differ from UI_EN), page (copy that replaces the APPS entry; English has
# none), guide_link, faq [(question, [blocks])], guide (a how-to page; here it is
# the stair layout, the tool people search for).
#
# Copy rules: plain sentences, one idea each. "Pay once, no subscription" early.
# Never name the handheld calculator this app replaces, or its maker.

L = {
    "name": "English",
    "path": "",
    "og_locale": "en_US",
    "ui": {
        "summary": "The limits the app checks",
    },
    "guide_link": "How to lay out a stair with Jobsite Calc",
    "faq": [
        ("Is Jobsite Calc a one-time purchase?", [
            "Yes. The app is free to download: the calculator, the conversions and the "
            "tape cost nothing. One in-app purchase unlocks the tools, which are stairs, "
            "rafters, roof, concrete, materials and angles. There is no subscription and "
            "nothing renews. The unlock is shared with your family through Family Sharing.",
        ]),
        ("How do I enter feet, inches and fractions?", [
            "Type 12, Feet, 3, Inch, 1, /, 2 and the display reads 12' 3-1/2\". A number "
            "on its own counts as inches; Settings can make it feet, millimetres or "
            "centimetres instead. With the metric keys turned on you can mix metres and "
            "inches in one calculation, and the result comes out in the unit you choose.",
            "The whole expression stays on screen while you type, with parentheses, so "
            "you can see what you entered before you press equals.",
        ]),
        ("How does the stair calculation work?", [
            "Enter the total rise, floor to floor. The app divides it into the fewest "
            "risers that stay under the riser limit, 7-3/4 inches by default, and gives "
            "the riser height, the treads, the total run, the stringer length, the angle "
            "and the stairwell opening. A line turns green when the stair meets the "
            "riser, tread and headroom limits, and red when it doesn't. The limits are "
            "yours to change in Settings.",
            "[Step by step](guide).",
        ]),
        ("Which rafters can it work out?", [
            "Common rafters from a pitch and a run, regular and irregular hips and "
            "valleys, and the jack rafters at your spacing, each with the plumb and "
            "level cuts. The pitch can be 7/12, degrees or a percentage. The Roof tool "
            "turns a plan area and a pitch into squares, bundles and sheets, and the "
            "rake wall rows give the stud lengths along a gable.",
        ]),
        ("Does it work in metric?", [
            "Yes. Turn on the metric keys in Settings for m, cm and mm, enter any mix of "
            "units in one calculation, and tap the unit on the result to convert it. "
            "Concrete can be shown in cubic metres and bags of 25 kg, and the stair and "
            "rafter tools take metric input too.",
        ]),
        ("Does anything leave my iPhone?", [
            "No. The app has no network code and makes no network connections. There is "
            "no account, no analytics and no ads. The one purchase goes through the App "
            "Store, and Apple handles it. [Privacy policy](privacy).",
        ]),
    ],
    "guide": {
        "slug": "stair-layout",
        "title": "How to lay out a stair stringer: risers, treads and the code check",
        "description": "Step by step: measure the total rise, enter it in Jobsite Calc, "
                       "read the risers, treads, stringer length and stairwell opening, "
                       "check the stair against code, and mark the stringer.",
        "lead": "A stair starts with one measurement, the total rise. From it the app "
                "gives the number of risers, their height, the treads, the total run, "
                "the stringer length, the angle and the stairwell opening, and checks "
                "them against the code limits. Here is how to use it.",
        "choose": [
            ("Riser", "7-3/4 in at most"),
            ("Tread", "10 in at least"),
            ("Headroom", "6 ft 8 in at least"),
        ],
        "steps": [
            ("Measure the total rise",
             "Measure straight up from the finished floor below to the finished floor "
             "above. Count the flooring that will go on top of each level: the stair is "
             "laid out to the finished surfaces, not to the subfloor."),
            ("Open Stairs",
             "In Jobsite Calc, tap Tools, then **Stairs**. The riser limit, the tread "
             "depth and the headroom are filled in with the usual code limits. You can "
             "change them in Settings."),
            ("Enter the total rise",
             "Type it the way you read it on the tape, for example 9' 1\". The app works "
             "out the stair as you type."),
            ("Read the risers",
             "The app uses the fewest risers that keep each one under the limit, all the "
             "same height. For 9' 1\" that is 15 risers of 7-1/4\"."),
            ("Treads and total run",
             "There is one tread fewer than risers. 14 treads of 10\" make a total run of "
             "11' 8\". If you have less room, enter the total run you have: the app "
             "shortens the treads to fit, and the code check tells you if they get too "
             "short."),
            ("Check the code line",
             "Green means every riser is at most 7-3/4\", every tread at least 10\" and "
             "the headroom at least 6' 8\". Red names the limit that fails. Local codes "
             "differ, so set your own limits in Settings."),
            ("Stairwell opening",
             "The app also gives the length of the floor opening that keeps the headroom, "
             "using the floor thickness from Settings. Check it against the framing "
             "before you cut."),
            ("Mark and cut the stringer",
             "Set a framing square to the riser height and the tread depth and step it "
             "along the stringer, once per riser. The stringer length on screen runs "
             "from the first riser to the last, so buy stock longer than that. Drop the "
             "bottom of the stringer by one tread thickness, so the first and last steps "
             "come out even once the treads are on."),
        ],
        "tips": [
            ("All risers are the same",
             "Codes allow only 3/8\" between the tallest and the shortest riser in a "
             "flight. The app gives one height; keep every riser to it."),
            ("The run comes from the treads",
             "Total run is treads times tread depth. A nosing sticks out past each "
             "riser but does not change the run."),
            ("Pick your fraction",
             "The app rounds to 1/16\" by default. Choose 1/8\" or 1/32\" in Settings, "
             "or decimals if you prefer."),
            ("The limits are the usual residential ones",
             "A 7-3/4\" riser, a 10\" tread and 6' 8\" of headroom are the limits most "
             "US residential codes use. Commercial stairs and other countries differ. "
             "Change the limits in Settings and the check follows."),
        ],
        "updated": "Written for Jobsite Calc 1.0, October 2026.",
        "cta_title": "Lay out the next stair in seconds",
        "cta_text": "Jobsite Calc works out the risers, treads, stringer and code check "
                    "from the total rise, on your iPhone, with no internet. Pay once, "
                    "no subscription.",
    },
}
