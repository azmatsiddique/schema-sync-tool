import pandas as pd
from schema_sync.infer import infer_schema
import json

def test_inference():
    # Create sample data with date and email
    data = {
        'id': [1, 2],
        'join_date': ['2023-01-01', '2023-01-02'],
        'email': ['alice@example.com', 'bob@example.com'],
        'optional': ['value', None]
    }
    df = pd.DataFrame(data)
    df.to_csv('test_advanced.csv', index=False)
    
    schema = infer_schema('test_advanced.csv')
    print(json.dumps(schema, indent=2))
    
    # Assertions
    properties = schema['properties']
    assert properties['join_date']['format'] == 'date-time'
    assert properties['email']['format'] == 'email'
    assert 'optional' not in schema['required']
    print("\nSUCCESS: Inference logic verification passed!")

if __name__ == "__main__":
    test_inference()
