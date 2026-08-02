---
type: "concept"
title: "gRPC Status Codes"
description: "The gRPC error model and status semantics"
tags: ["grpc", "status-codes", "errors", "rpc", "error-handling"]
timestamp: "2026-08-01T00:00:00Z"
status: "growing"
source: ["https://grpc.io/docs/guides/status-codes/", "https://github.com/grpc/grpc/blob/master/doc/statuscodes.md"]
---

# gRPC Status Codes

## Summary
gRPC uses a small set of canonical status codes — OK, InvalidArgument, NotFound, Unavailable, DeadlineExceeded, and friends — instead of HTTP status classes. Codes are part of the RPC contract, carried in the trailing metadata of the HTTP/2 response, and mapped to language-native exceptions by generated stubs.

## Details
- The code list: OK(0), Canceled, Unknown, InvalidArgument, DeadlineExceeded, NotFound, AlreadyExists, PermissionDenied, ResourceExhausted, FailedPrecondition, Aborted, OutOfRange, Unimplemented, Internal, Unavailable, DataLoss, Unauthenticated.
- Wire format: the status code and message travel in the HTTP/2 trailer (grpc-status, grpc-message) after all response messages, so errors are terminal stream events.
- Error details: richer structured details use the google.rpc.Status and error_details proto types (RetryInfo, ErrorInfo, BadRequest, QuotaFailure) transported via grpc-status-details-bin.
- Retry semantics: Unavailable, DeadlineExceeded, and Aborted are commonly retryable; InvalidArgument and NotFound are permanent client errors.
- Mapping: each language maps codes to exceptions (gRPCError in Python, StatusRuntimeException in Java), preserving the code across the boundary.
- Gateway translation: grpc-gateway maps gRPC codes to HTTP status codes (for example NotFound -> 404, Unauthenticated -> 401) with configurable mapping.

## Related
- [[wiki/api-protocols/grpc|gRPC]] — status codes are gRPC's error contract
- [[wiki/api-protocols/grpc-streaming|gRPC Streaming]] — streams end with a terminal status
- [[wiki/api-protocols/grpc-gateway|gRPC Gateway]] — mapping gRPC codes to HTTP status
- [[wiki/api-protocols/error-contract-design|Error Contract Design]] — consistent codes across RPC and REST
- [[wiki/api-protocols/retry-policies|Retry Policies]] — retryable status codes drive policies
