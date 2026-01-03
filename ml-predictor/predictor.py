import torch
import torch.nn as nn
import numpy as np

# Must match training architecture
class LSTMModel(nn.Module):
    def __init__(self):
        super().__init__()
        self.lstm = nn.LSTM(input_size=1, hidden_size=50, num_layers=1)
        self.fc = nn.Linear(50, 1)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[-1])

class ResourcePredictor:
    def __init__(self, model_path="model.pt"):
        self.model = LSTMModel()
        self.model.load_state_dict(torch.load(model_path))
        self.model.eval()

    def predict_time_to_exhaustion(self, series):
        """
        series: list of historical utilization values (normalized 0–1)
        """
        x = torch.tensor(series, dtype=torch.float32).view(len(series), 1, 1)
        with torch.no_grad():
            prediction = self.model(x)
        return float(prediction.item())

if __name__ == "__main__":
    predictor = ResourcePredictor()
    sample = np.linspace(0.3, 0.85, 50)
    print("Predicted exhaustion delta:", predictor.predict_time_to_exhaustion(sample))
