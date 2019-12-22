# 7. WebAuthn Relying Party Operations

- https://www.w3.org/TR/webauthn/#rp-operations

Upon successful execution of create() or get(), 
the WebAuthn Relying Party's script receives a PublicKeyCredential 
containing an AuthenticatorAttestationResponse or AuthenticatorAssertionResponse structure, 
respectively, from the client.

It must then deliver the contents of this structure to the Relying Party server, 
using methods outside the scope of this specification. 

This section describes the operations that the Relying Party must perform upon receipt of these structures.
