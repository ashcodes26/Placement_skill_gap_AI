# Data Import Specification

MVP sources: CSV and Excel (.xlsx).

Pipeline: Upload → File Type Validation → Parse → Detect Headers → Map Columns → Normalize → Validate → Detect Duplicates → Preview → Confirm → Batch Insert → Import Report.

Required fields include student_id, first_name, last_name, email, and program or department.
