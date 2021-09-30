__author__ = "uberfastman"
__email__ = "uberfastman@uberfastman.dev"

usage_message = \
    "\n" \
    "Fantasy Football Report application usage:\n" \
    "\n" \
    "    python main.py [optional_parameters]\n" \
    "\n" \
    "  Options:\n" \
    "      -h, --help                            Print command line usage message.\n" \
    "      -a, --auto-run                        Automatically run the report using the default week.\n" \
    "\n" \
    "    Generate report:\n" \
    "      -f, --fantasy-platform <platform>     Fantasy football platform on which league for report is hosted. " \
                                                 "Currently supports: \"yahoo\", \"fleaflicker\" \n" \
    "      -l, --league-id <league_id>           Fantasy Football league ID.\n" \
    "      -w, --week <chosen_week>              Chosen week for which to generate report.\n" \
    "      -g, --game-id <chosen_game_id>        Chosen fantasy game id for which to generate report. Defaults to " \
                                                 "\"nfl\", which is interpreted as the current season if using " \
                                                 "Yahoo.\n" \
    "      -y, --year <chosen_year>              Chosen year (season) of the league for which a report is being " \
                                                 "generated.\n" \
    "\n" \
    "    Configuration:\n" \
    "      -c, --config-file <config_file_path>  System file path (including file name) for .ini file to be used for " \
                                                 "configuration.\n" \
    "      -s, --save-data                       Save all retrieved data locally for faster future report " \
                                                 "generation.\n" \
    "      -r, --refresh-web-data                Refresh all web data from external APIs (such as bad boy and beef " \
                                                 "data).\n" \
    "      -p, --playoff-prob-sims               Number of Monte Carlo playoff probability simulations to run.\n" \
    "      -b, --break-ties                      Break ties in metric rankings.\n" \
    "      -q, --disqualify-ce                   Automatically disqualify teams ineligible for coaching efficiency " \
                                                 "metric.\n" \
    "\n" \
    "    For Developers:\n" \
    "      -d, --dev-offline                     Run OFFLINE for development. Must have previously run report with " \
                                                 "-s option.\n" \
    "      -t, --test                            Generate TEST report.\n"
