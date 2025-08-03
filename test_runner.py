import subprocess
import re
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')

# Read the testcases.txt file
with open("testcases.txt", "r", encoding="utf-8") as f:
    content = f.read()

# Remove old test results if present (everything after first === Test Case Results ===)
content = content.split("=== Test Case Results ===")[0].rstrip()

# Extract InputCopy block and OutputCopy block
input_match = re.search(r'(InputCopy\s*\n)(.*?)(\nOutputCopy)', content, re.DOTALL)
output_match = re.search(r'(OutputCopy\s*\n)(.*)', content, re.DOTALL)

if not input_match or not output_match:
    print("❌ InputCopy or OutputCopy block not found in testcases.txt")
    exit(1)

input_header = input_match.group(1)  # "InputCopy\n"
input_block = input_match.group(2).strip()

output_header = output_match.group(1)  # "OutputCopy\n"
output_block = output_match.group(2).strip()

# Prepare input and expected output lines
input_lines = [line.strip() for line in input_block.splitlines() if line.strip() != ""]
expected_output_lines = [line.strip() for line in output_block.splitlines() if line.strip() != ""]

# Run your program with the input
result = subprocess.run(
    ["t.exe"],             # Replace with your executable path if needed
    input="\n".join(input_lines),
    capture_output=True,
    text=True
)

# Get actual output lines from your program
output_lines = result.stdout.strip().splitlines()

max_lines = max(len(output_lines), len(expected_output_lines))

# Prepare the test result report
report_lines = ["\n\n=== Test Case Results ===\n", "Expected Output       Your Output           Result\n"]

for i in range(max_lines):
    expected_line = expected_output_lines[i] if i < len(expected_output_lines) else "<missing>"
    user_line = output_lines[i] if i < len(output_lines) else "<missing>"

    matched = expected_line.strip() == user_line.strip()
    result_mark = "-> ✅" if matched else "-> ❌"

    report_lines.append(f"{expected_line:<22}{user_line:<22}{result_mark}\n")

# Write back the file:
# - InputCopy block unchanged
# - OutputCopy block unchanged (fixed expected output)
# - Append latest test result report below
with open("testcases.txt", "w", encoding="utf-8") as f:
    f.write(input_header)
    f.write(input_block + "\n")
    f.write(output_header)
    f.write(output_block + "\n")
    f.writelines(report_lines)

print("✅ Latest test results saved in testcases.txt")
