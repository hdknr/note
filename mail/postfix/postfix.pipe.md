# [Postfix manual - pipe(8)](http://www.postfix.org/pipe.8.html)

- [pipe](http://www.postfix.org/pipe.8.html)


## flags:  `flags=BDFORXhqu.>@ (オプション)

Optional message processing flags. By default, a message is copied unchanged.


B(ブランク行追加):

- Append a blank line at the end of each message. 
- This is required by some mail user agents that recognize "From " lines 
  only when preceded by a blank line.

D(`Delivered-To`の追加):

- Prepend a "Delivered-To: recipient" message header with the envelope recipient address. 
- Note: for this to work, 
  the `transport_destination_recipient_limit` must be 1 
  (see SINGLE-RECIPIENT DELIVERY above for details).

- The D flag also enforces loop detection (Postfix 2.5 and later): 

  - if a message already contains a Delivered-To: header with the same recipient address, 
    then the message is returned as undeliverable. 
    The address comparison is case insensitive.

- This feature is available as of Postfix 2.0.

F(Fromエンベロープの追加):

- Prepend a "From sender time_stamp" envelope header to the message content. 
  This is expected by, for example, UUCP software.

O(`X-Original-To`の追加):

- Prepend an "X-Original-To: recipient" message header with the recipient address as given to Postfix. 
- Note: for this to work, 
  the `transport_destination_recipient_limit` must be 1 
  (see SINGLE-RECIPIENT DELIVERY above for details).

- This feature is available as of Postfix 2.0.

R(`Return-Path`の追加):

- Prepend a Return-Path: message header with the envelope sender address.

X(最終デリバリ):

- Indicate that the external command performs final delivery. 
  This flag affects the status reported in "success" DSN 
  (delivery status notification) messages, 
  and changes it from "relayed" into "delivered".

- This feature is available as of Postfix 2.5.

h:

- Fold the command-line $original_recipient and $recipient address domain part 
  (text to the right of the right-most @ character) to lower case; 
  fold the entire command-line $domain and $nexthop host 
  or domain information to lower case. 

  This is recommended for delivery via UUCP.

q(クオート):

- Quote white space and other special characters in the command-line $sender, 
  $original_recipient and $recipient address localparts 
  (text to the left of the right-most @ character), 
  according to an 8-bit transparent version of RFC 822. 
  
  This is recommended for delivery via UUCP or BSMTP.

- The result is compatible with the address parsing of command-line recipients 
  by the Postfix sendmail(1) mail submission command.
- The q flag affects only entire addresses, 
  not the partial address information from the $user, $extension or $mailbox command-line macros.

u:

- Fold the command-line $original_recipient and $recipient address localpart 
  (text to the left of the right-most @ character) to lower case. 
  
  This is recommended for delivery via UUCP.

`.`:

- Prepend "." to lines starting with ".". 

  This is needed by, for example, BSMTP software.


`>`:

- Prepend ">" to lines starting with "From ". 
  This is expected by, for example, UUCP software.

