from schema_sync import infer_schema, validate_data, compare_schemas
import json
import os

def test_api():
    print("Testing API...")
    
    # Test infer
    print("Inferring schema...")
    schema = infer_schema("users.csv")
    print("Schema inferred successfully.")
    
    with open("schema_api.json", "w") as f:
        json.dump(schema, f, indent=2)
        
    # Test validate
    print("Validating data...")
    valid = validate_data("users.csv", "schema_api.json")
    if valid:
        print("Validation successful.")
    else:
        print("Validation failed.")
        
    # Test compare
    print("Comparing schemas...")
    diff = compare_schemas("schema_api.json", "schema_api.json")
    print(f"Diff (should be empty): {diff}")
    
    # Create a modified schema to test compare
    schema_mod = schema.copy()
    schema_mod["properties"]["new_col"] = {"type": "string"}
    with open("schema_mod.json", "w") as f:
        json.dump(schema_mod, f, indent=2)
        
    diff_mod = compare_schemas("schema_api.json", "schema_mod.json")
    print(f"Diff (should have new_col): {diff_mod}")

if __name__ == "__main__":
    test_api()
