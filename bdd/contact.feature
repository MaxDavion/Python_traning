Scenario Outline: Add new contact
  Given a contact list
  Given a contact with <firstname>, <lastname>, <address>
  When I add the contact to the list
  Then the new contact list is equal to the old list with added contact

  Examples:
  | firstname | lastname | address |
  | firstname2 | lastname2 | address2 |

Scenario: Delete a contact
  Given a non-empty contact list
  Given a random contact from the list
  When I delete the contact from the list
  Then the new contact list is equal to the old list without deleted contact


Scenario Outline: Edit a contact
  Given a non-empty contact list
  Given a random contact from the list
  Given a contact with <firstname>, <lastname>, <address>
  When I edit the contact from the list
  Then the new contact list is equal to the old list with edit contact

  Examples:
  | firstname | lastname | address |
  | firstname2 | lastname2 | address2 |