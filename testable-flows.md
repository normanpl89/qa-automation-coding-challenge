 @search_user_enter
  Scenario: Search a User By pressing Enter Key.
    Given I logged on the Application page.
    When I logged I validate the Header of the Page "Get Github Repos".
    Then I enter a valid user "normanpl89" and tap enter.
    And Get the "Success!" message.
    And I validate the result is equal to 8.
    Then I attach an screenshot of the result.

  @search_user_go
  Scenario: Search a User by clicking Go.
    Given I logged on the Application page.
    When I logged I validate the Header of the Page "Get Github Repos".
    Then I enter a valid user "normanpl89" and click Go.
    And Get the "Success!" message.
    And I validate the result is equal to 8.
    Then I attach an screenshot of the result.

  @negative_search_flow_go
  Scenario: Search a User Go flow W/no Existing user.
    Given I logged on the Application page.
    When I logged I validate the Header of the Page "Get Github Repos".
    Then I enter a valid user "royunuet" and click Go.
    And Get the error message "Github user not found".
    And I validate the "No repos" message displayed.
    Then I attach an screenshot of the result.

  @negative_search_enter_flow
  Scenario: Search a User Enter flow W/no Existing user.
    Given I logged on the Application page.
    When I logged I validate the Header of the Page "Get Github Repos".
    Then I enter a valid user "royunuet" and tap enter.
    And Get the error message "Github user not found".
    And I validate the "No repos" message displayed.
    Then I attach an screenshot of the result.

  @negative_search_enter_flow
  Scenario: Search a w/empty field user.
    Given I logged on the Application page.
    When I logged I validate the Header of the Page "Get Github Repos".
    Then I enter a valid user " " and tap enter.
    And Get the error message "Github user not found".
    And I validate the "No repos" message displayed.
    Then I attach an screenshot of the result.




(Add your list of flows here)
