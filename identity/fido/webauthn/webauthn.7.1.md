# 7.1. Registering a new credential

- https://www.w3.org/TR/webauthn/#rp-operations

When registering a new credential,
represented by an AuthenticatorAttestationResponse structure response 
and an AuthenticationExtensionsClientOutputs structure clientExtensionResults, 
as part of a registration ceremony, 
a Relying Party MUST proceed as follows:

## 1. Let JSONtext be the result of running UTF-8 decode on the value of response.clientDataJSON.

    Note: Using any implementation of UTF-8 decode is acceptable 
    as long as it yields the same result as that yielded by the UTF-8 decode algorithm. 

    In particular, any leading byte order mark (BOM) MUST be stripped.

## 2 . Let C, the client data claimed as collected during the credential creation, be the result of running an implementation-specific JSON parser on JSONtext.

Note: C may be any implementation-specific data structure representation, as long as C’s components are referenceable, as required by this algorithm.

## 3. Verify that the value of C.type is webauthn.create.

## 4. Verify that the value of C.challenge matches the challenge that was sent to the authenticator in the create() call.

## 5. Verify that the value of C.origin matches the Relying Party's origin.

## 6. Verify that the value of C.tokenBinding.status matches the state of Token Binding for the TLS connection over which the assertion was obtained. If Token Binding was used on that TLS connection, also verify that C.tokenBinding.id matches the base64url encoding of the Token Binding ID for the connection.

## 7. Compute the hash of response.clientDataJSON using SHA-256.

## 8. Perform CBOR decoding on the attestationObject field of the AuthenticatorAttestationResponse structure to obtain the attestation statement format fmt, the authenticator data authData, and the attestation statement attStmt.

## 9. Verify that the RP ID hash in authData is indeed the SHA-256 hash of the RP ID expected by the RP.

## 10. Verify that the User Present bit of the flags in authData is set.

## 11. If user verification is required for this registration, verify that the User Verified bit of the flags in authData is set.

## 12. Verify that the values of the client extension outputs in clientExtensionResults and the authenticator extension outputs in the extensions in authData are as expected, considering the client extension input values that were given as the extensions option in the create() call. In particular, any extension identifier values in the clientExtensionResults and the extensions in authData MUST be also be present as extension identifier values in the extensions member of options, i.e., no extensions are present that were not requested. In the general case, the meaning of "are as expected" is specific to the Relying Party and which extensions are in use.

Note: Since all extensions are OPTIONAL for both the client and the authenticator, the Relying Party MUST be prepared to handle cases where none or not all of the requested extensions were acted upon.

## 13. Determine the attestation statement format by performing a USASCII case-sensitive match on fmt against the set of supported WebAuthn Attestation Statement Format Identifier values. The up-to-date list of registered WebAuthn Attestation Statement Format Identifier values is maintained in the in the IANA registry of the same name [WebAuthn-Registries].

## 14. Verify that attStmt is a correct attestation statement, conveying a valid attestation signature, by using the attestation statement format fmt’s verification procedure given attStmt, authData and the hash of the serialized client data computed in step 7.

Note: Each attestation statement format specifies its own verification procedure. See §8 Defined Attestation Statement Formats for the initially-defined formats, and  [WebAuthn-Registries] for the up-to-date list.

## 15. If validation is successful, obtain a list of acceptable trust anchors (attestation root certificates or ECDAA-Issuer public keys) for that attestation type and attestation statement format fmt, from a trusted source or from policy. For example, the FIDO Metadata Service  [FIDOMetadataService] provides one way to obtain such information, using the aaguid in the attestedCredentialData in authData.

## 16. Assess the attestation trustworthiness using the outputs of the verification procedure in step 14, as follows:

- If self attestation was used, check if self attestation is acceptable under Relying Party policy.
- If ECDAA was used, verify that the identifier of the ECDAA-Issuer public key used is included in the set of acceptable trust anchors obtained in step 15.
- Otherwise, use the X.509 certificates returned by the verification procedure to verify that the attestation public key correctly chains up to an acceptable root certificate.

## 17. Check that the credentialId is not yet registered to any other user. If registration is requested for a credential that is already registered to a different user, the Relying Party SHOULD fail this registration ceremony, or it MAY decide to accept the registration, e.g. while deleting the older registration.

## 18. If the attestation statement attStmt verified successfully and is found to be trustworthy, then register the new credential with the account that was denoted in the options.user passed to create(), by associating it with the credentialId and credentialPublicKey in the attestedCredentialData in authData, as appropriate for the Relying Party's system.

## 19. If the attestation statement attStmt successfully verified but is not trustworthy per step 16 above, the Relying Party SHOULD fail the registration ceremony.

NOTE: However, if permitted by policy, the Relying Party MAY register the credential ID and credential public key but treat the credential as one with self attestation (see §6.4.3 Attestation Types). If doing so, the Relying Party is asserting there is no cryptographic proof that the public key credential has been generated by a particular authenticator model. See  [FIDOSecRef] and [UAFProtocol] for a more detailed discussion.

Verification of attestation objects requires that the Relying Party has a trusted method of determining acceptable trust anchors in step 15 above. Also, if certificates are being used, the Relying Party MUST have access to certificate status information for the intermediate CA certificates. The Relying Party MUST also be able to build the attestation certificate chain if the client did not provide this chain in the attestation information.