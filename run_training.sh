#!/bin/bash
# Quick training script for Linux/Mac

echo "========================================"
echo "Customer Churn Prediction - Training"
echo "========================================"
echo ""

echo "Checking Python installation..."
python3 --version
if [ $? -ne 0 ]; then
    echo "ERROR: Python not found!"
    exit 1
fi

echo ""
echo "Starting training pipeline..."
echo ""

python3 main.py

echo ""
echo "========================================"
echo "Training completed!"
echo "Check artifacts/ directory for results"
echo "========================================"
echo ""
