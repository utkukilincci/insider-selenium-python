#INSIDER UI AUTOMATION (SELENIUM / PYTHON)

## Requirements

1. [Download](https://www.python.org/downloads/) python
2. Run this command your terminal for downloading pytest with [pip](https://pip.pypa.io/en/stable/installation/)
    * `pip3 install pytest` or `pip install pytest`
    
## Running Tests

1. You can run tests with `pytest` command in project terminal
2. You can run tests at Firefox like this `pytest --browser firefox`

## Case

1. Visit https://useinsider.com/ and check Insider home page is opened or not
2. Select “More” menu in navigation bar, select “Careers” and check Career page, its
Locations, Teams and Life at Insider blocks are opened or not
3. Click “See All Teams”, select Quality Assurance, click “See all QA jobs”, filter jobs by
Location - Istanbul, Turkey and department - Quality Assurance, check presence of
jobs list
4. Check that all jobs’ Position contains “Quality Assurance”, Department contains
“Quality Assurance”, Location contains “Istanbul, Turkey” and “Apply Now” button
5. Click “Apply Now” button and check that this action redirects us to Lever Application
form page
   
## Notes

1. In the beginning of test, old screenshots will be removed
2. Screenshots will be taken if test fails one of steps