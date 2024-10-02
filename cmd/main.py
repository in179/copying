import os
import logging
from cli import App, BoolFlag, StringFlag
from browser import PickBrowsers
from logger import Default, Configure
from utils.fileutil import CompressDir

browser_name = ""
output_dir = ""
output_format = "csv"
verbose = False
compress = False
profile_path = ""
is_full_export = True

def main():
    execute()

def execute():
    app = App(
        name="copying",
        usage="Export passwords|bookmarks|cookies|history|credit cards|download history|localStorage|extensions from browser",
        usage_text="[copying -b chrome -f json --dir results --zip]\nExport all browsing data (passwords/cookies/history/bookmarks) from browser\nGithub Link: https://github.com/in179/copying",
        version="0.4.6",
        flags=[
            BoolFlag(name="verbose", aliases=["vv"], destination=verbose, value=False, usage="verbose"),
            BoolFlag(name="compress", aliases=["zip"], destination=compress, value=False, usage="compress result to zip"),
            StringFlag(name="browser", aliases=["b"], destination=browser_name, value="all", usage="available browsers: all|" + browser.Names()),
            StringFlag(name="results-dir", aliases=["dir"], destination=output_dir, value="results", usage="export dir"),
            StringFlag(name="format", aliases=["f"], destination=output_format, value="csv", usage="output format: csv|json"),
            StringFlag(name="profile-path", aliases=["p"], destination=profile_path, value="", usage="custom profile dir path, get with chrome://version"),
            BoolFlag(name="full-export", aliases=["full"], destination=is_full_export, value=True, usage="is export full browsing data"),
        ],
        hide_help_command=True,
        action=lambda c: action(c)
    )
    try:
        app.run(os.sys.argv)
    except Exception as err:
        raise err

def action(c):
    global verbose
    if verbose:
        Default.SetVerbose()
        Configure(Default)
    
    browsers, err = PickBrowsers(browser_name, profile_path)
    if err:
        logging.error("pick browsers error: %s", err)

    for b in browsers:
        data, err = b.BrowsingData(is_full_export)
        if err:
            logging.error("get browsing data error: %s", err)
            continue
        data.Output(output_dir, b.Name(), output_format)

    if compress:
        err = CompressDir(output_dir)
        if err:
            logging.error("compress error: %s", err)
        logging.info("compress success")

if __name__ == "__main__":
    main()

