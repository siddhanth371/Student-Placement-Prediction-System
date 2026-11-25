print("Model inspection script is running!")

from src.config import MODEL_PATH, PREPROCESSOR_PATH

print("Model path:", MODEL_PATH)
print("Preprocessor path:", PREPROCESSOR_PATH)

from src.utils import load_pickle

model = load_pickle(MODEL_PATH)
preprocessor = load_pickle(PREPROCESSOR_PATH)

print("\n========== MODEL DETAILS ==========")
print("Algorithm:", type(model).__name__)
print("Parameters:", model.get_params())

print("\n========== PREPROCESSOR DETAILS ==========")
print("Type:", type(preprocessor).__name__)

if hasattr(preprocessor, "named_steps"):
    print("Steps:", list(preprocessor.named_steps.keys()))

print("\nInspection completed successfully!")                                   