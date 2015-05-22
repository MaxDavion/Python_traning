Scenario: Add new group
  Given a group list
  Given a group with <name>, <header>, <footer>
  When I add the group to the list
  Then the new group list is equal to the old list with added group

  Examples:
  | name | header | footer |
  | name 2 | header 2 | footer 2|