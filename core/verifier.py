from dataclasses import dataclass
import json

@dataclass
class VerifyResult:
    status: str
    checks_passed: list
    checks_failed: list
    message: str

def print_verify_result(result):
    colors = {
        "PASS": "\033[92m",
        "WARN": "\033[93m",
        "FAIL": "\033[91m"
    }

    reset = "\033[0m"
    color = colors.get(result.status, "")

    print(f"{color}{result.status}{reset}")
    print(result.message)


def verify_step_output(step, output: str) -> VerifyResult:
    passed = []
    failed = []

    if output and len(output.strip()) > 0:
        passed.append("non_empty")
    else:
        failed.append("non_empty")

    if len(output) >= 20:
        passed.append("min_length_20")
    else:
        failed.append("min_length_20")

    banned = [
        "as an ai",
        "i cannot",
        "i am unable",
        "i don't have access",
        "i apologize"
    ]
    if not any(b in output.lower() for b in banned):
        passed.append("no_hallucination_phrases")
    else:
        failed.append("no_hallucination_phrases")

    if isinstance(step, dict) and step.get("expects") == "json":
        try:
            json.loads(output)
            passed.append("valid_json")
        except:
            failed.append("valid_json")

    if isinstance(step, dict) and step.get("expects") == "email":
        if "@" in output:
            passed.append("valid_email_format")
        else:
            failed.append("valid_email_format")

    if len(output) < 10 or len(output) > 5000:
        failed.append("length_sanity")
    else:
        passed.append("length_sanity")

    status = "PASS" if len(failed) == 0 else ("WARN" if len(failed) <= 2 else "FAIL")

    return VerifyResult(
        status=status,
        checks_passed=passed,
        checks_failed=failed,
        message=f"{status}: {len(passed)} passed, {len(failed)} failed"
    )
