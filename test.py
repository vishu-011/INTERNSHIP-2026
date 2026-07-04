from hpp import predict_rent

sample = {
    "BHK": 2,
    "Size": 1200,
    "Floor": "1 out of 3",
    "Area Type": "Super Area",
    "Area Locality": "Bandel",
    "City": "Kolkata",
    "Furnishing Status": "Semi-Furnished",
    "Tenant Preferred": "Family",
    "Bathroom": 2,
    "Point of Contact": "Contact Owner",
}

prediction = predict_rent(sample)
assert prediction > 0
print("Prediction smoke test passed:", prediction)