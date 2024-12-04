Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro

Background:
    Given I open the url "https://byjus.com/herons-calculator/"


Scenario: I can calculate the area of a triangle
    Then I expect that element "h2" contains any text

Scenario: I can input a 
    When I add "1" to the inputfield "#a"
    Then I expect that element "#a" contains the text "1"

Scenario: I can input b 
    When I add "1" to the inputfield "#b"
    Then I expect that element "#b" contains the text "1"

Scenario: I can input c 
    When I add "1" to the inputfield "#c"
    Then I expect that element "#c" contains the text "1"


Scenario: I can input 
    When I add "1" to the inputfield "#a"
    When I add "1" to the inputfield "#b"
    When I add "1" to the inputfield "#c"
    When I click on the button ".clcbtn"
    Then I expect that element "#_e" contains the text "1.5"
    
Scenario: I get an error
    When I add "a" to the inputfield "#a"
    When I add "1" to the inputfield "#b"
    When I add "1" to the inputfield "#c"
    When I click on the button ".clcbtn"
    Then I expect that a alertbox is opened

