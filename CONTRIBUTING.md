# Contributing to Customer Churn Prediction

First off, thank you for considering contributing to this project! 🎉

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Development Setup](#development-setup)
- [Style Guidelines](#style-guidelines)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

---

## 📜 Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow. Be respectful, inclusive, and professional.

---

## 🤝 How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When creating a bug report, include:

- **Clear title and description**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Screenshots** (if applicable)
- **Environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Clear title and description**
- **Use case and motivation**
- **Possible implementation approach**
- **Alternative solutions considered**

### Code Contributions

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Make your changes**
4. **Write tests**
5. **Commit your changes**: `git commit -m 'Add some AmazingFeature'`
6. **Push to branch**: `git push origin feature/AmazingFeature`
7. **Open a Pull Request**

---

## 🛠️ Development Setup

```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/customer-churn-prediction.git
cd customer-churn-prediction

# Add upstream remote
git remote add upstream https://github.com/ORIGINAL_OWNER/customer-churn-prediction.git

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Install development dependencies
pip install -r requirements.txt
pip install -r requirements-dev.txt  # If exists
```

---

## 📝 Style Guidelines

### Python Code Style

Follow **PEP 8** style guide:

```python
# Good
def calculate_churn_probability(features, model):
    """
    Calculate churn probability for given features.
    
    Args:
        features: Customer features
        model: Trained ML model
        
    Returns:
        float: Churn probability
    """
    return model.predict_proba(features)[:, 1]

# Bad
def calc_prob(f,m):
    return m.predict_proba(f)[:,1]
```

### Docstrings

Use Google-style docstrings:

```python
def train_model(X_train, y_train, model_name):
    """
    Train machine learning model.
    
    Args:
        X_train (np.ndarray): Training features
        y_train (np.ndarray): Training labels
        model_name (str): Name of model to train
        
    Returns:
        sklearn.Model: Trained model instance
        
    Raises:
        ValueError: If model_name is not recognized
        CustomException: If training fails
        
    Example:
        >>> model = train_model(X, y, 'RandomForest')
    """
    pass
```

### Code Organization

```python
# Imports (organized)
# 1. Standard library
import os
import sys

# 2. Third-party
import pandas as pd
import numpy as np

# 3. Local
from src.logger import logging
from src.exception import CustomException

# Constants
MAX_ITERATIONS = 1000
DEFAULT_THRESHOLD = 0.5

# Classes and functions
class MyClass:
    pass

def my_function():
    pass
```

---

## 📌 Commit Guidelines

### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, etc.)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks

### Examples

```bash
# Good
git commit -m "feat(model): add XGBoost hyperparameter tuning"
git commit -m "fix(app): resolve streamlit caching issue"
git commit -m "docs(readme): update installation instructions"

# Bad
git commit -m "changes"
git commit -m "fixed bug"
```

---

## 🔄 Pull Request Process

### Before Submitting

1. **Update documentation** if needed
2. **Add tests** for new features
3. **Run all tests** and ensure they pass
4. **Update CHANGELOG.md** (if exists)
5. **Ensure code follows style guidelines**

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
- [ ] Tests pass locally
- [ ] New tests added
- [ ] Manual testing performed

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Documentation updated
- [ ] No new warnings
```

### Review Process

1. **Automated checks** must pass
2. **At least one approval** required
3. **Resolve all comments**
4. **Keep PR focused** on single feature/fix
5. **Squash commits** if requested

---

## 🧪 Testing

### Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_model_trainer.py

# Run with coverage
pytest --cov=src tests/
```

### Writing Tests

```python
# tests/test_example.py
import pytest
from src.components.model_trainer import ModelTrainer

def test_model_training():
    """Test model training functionality"""
    trainer = ModelTrainer()
    assert trainer is not None
    
def test_model_evaluation():
    """Test model evaluation"""
    # Test implementation
    pass
```

---

## 📚 Documentation

### Code Comments

```python
# Good - Explain WHY, not WHAT
# Use median imputation to handle outliers better than mean
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)

# Bad - States the obvious
# Fill missing values
df['TotalCharges'].fillna(df['TotalCharges'].median(), inplace=True)
```

### README Updates

When adding features, update:
- Feature list
- Usage examples
- Installation steps (if needed)
- Screenshots (if UI changed)

---

## 🎯 Areas for Contribution

### High Priority

- [ ] Unit tests for all components
- [ ] Integration tests
- [ ] API documentation
- [ ] Performance optimization
- [ ] Error handling improvements

### Medium Priority

- [ ] Additional ML models
- [ ] Feature engineering enhancements
- [ ] Dashboard improvements
- [ ] Data validation rules
- [ ] Logging enhancements

### Low Priority

- [ ] UI/UX improvements
- [ ] Code refactoring
- [ ] Documentation improvements
- [ ] Example notebooks
- [ ] Tutorial videos

---

## 🚀 Feature Requests

### Before Implementing

1. **Check existing issues** for duplicates
2. **Create an issue** to discuss
3. **Wait for feedback** from maintainers
4. **Get approval** before starting work

### Implementation Guidelines

1. **Keep it modular**: Follow existing architecture
2. **Maintain backward compatibility**: Don't break existing code
3. **Add configuration**: Use config.yaml for parameters
4. **Include tests**: Test new functionality
5. **Update docs**: Keep documentation current

---

## 🔍 Code Review Checklist

### For Reviewers

- [ ] Code follows project style
- [ ] Tests are included
- [ ] Documentation is updated
- [ ] No unnecessary changes
- [ ] Commit messages are clear
- [ ] No security issues
- [ ] Performance impact considered

### For Contributors

- [ ] Self-review completed
- [ ] Tests pass
- [ ] Documentation updated
- [ ] Code is commented
- [ ] No debug code left
- [ ] Dependencies documented
- [ ] CHANGELOG updated

---

## 📞 Getting Help

### Resources

- **Documentation**: Read README.md and other docs
- **Issues**: Check existing issues for similar problems
- **Discussions**: Use GitHub Discussions for questions

### Contact

- **GitHub Issues**: Technical problems
- **Email**: your.email@example.com
- **LinkedIn**: [Your Profile](https://linkedin.com/in/yourprofile)

---

## 🏆 Recognition

Contributors will be:
- Listed in CONTRIBUTORS.md
- Mentioned in release notes
- Credited in documentation

---

## 📜 License

By contributing, you agree that your contributions will be licensed under the same license as the project (MIT License).

---

Thank you for contributing! 🙏

**Happy Coding!** 🚀
