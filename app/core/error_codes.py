# app/core/error_codes.py
BAD_REQUEST = {"status": 400, "code": "BAD_REQUEST", "message": "요청 형식이 올바르지 않음"}
VALIDATION_FAILED = {"status": 400, "code": "VALIDATION_FAILED", "message": "필드 유효성 검사 실패"}
UNAUTHORIZED = {"status": 401, "code": "UNAUTHORIZED", "message": "인증 실패"}
TOKEN_EXPIRED = {"status": 401, "code": "TOKEN_EXPIRED", "message": "토큰 만료"}
FORBIDDEN = {"status": 403, "code": "FORBIDDEN", "message": "접근 권한 없음"}
RESOURCE_NOT_FOUND = {"status": 404, "code": "RESOURCE_NOT_FOUND", "message": "리소스 없음"}
USER_NOT_FOUND = {"status": 404, "code": "USER_NOT_FOUND", "message": "사용자 없음"}
DUPLICATE_RESOURCE = {"status": 409, "code": "DUPLICATE_RESOURCE", "message": "중복 데이터 존재"}
STATE_CONFLICT = {"status": 409, "code": "STATE_CONFLICT", "message": "리소스 상태 충돌"}
UNPROCESSABLE_ENTITY = {"status": 422, "code": "UNPROCESSABLE_ENTITY", "message": "처리할 수 없는 요청 내용"}
TOO_MANY_REQUESTS = {"status": 429, "code": "TOO_MANY_REQUESTS", "message": "요청 한도 초과"}
INTERNAL_SERVER_ERROR = {"status": 500, "code": "INTERNAL_SERVER_ERROR", "message": "서버 내부 오류"}
DATABASE_ERROR = {"status": 500, "code": "DATABASE_ERROR", "message": "DB 연동 오류"}
UNKNOWN_ERROR = {"status": 500, "code": "UNKNOWN_ERROR", "message": "알 수 없는 오류"}
