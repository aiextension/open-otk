"""
Open OTK (Open Ollama Toolkit)
Professional Python library for building AI applications with Ollama models

This library provides a complete development toolkit for integrating Ollama's local LLM models
into production-ready Python applications with full customization, experimentation, and GUI tools.

Author: Md. Abid Hasan Rafi (AI Extension)
License: MIT
"""

from .client import OllamaClient
from .models import ModelManager
from .chat import ChatSession
from .utils import (
    format_response,
    estimate_tokens,
    chunk_text,
    create_prompt_template
)
from .response_handlers import (
    ModelResponseHandler,
    AutoModelHandler,
    ModelType,
    ProcessedResponse,
    clean_thinking_tags,
    auto_clean_response
)
from .customization import (
    CustomizableModel,
    ModelConfig,
    ModelPresets,
    ModelBuilder,
    HookType,
    HookContext,
)
from .experimentation import (
    ModelExperiment,
    ModelPlayground,
    ABTest,
    ExperimentResult,
    ComparisonResult
)

__version__ = "1.0.0"
__author__ = "Md. Abid Hasan Rafi (AI Extension)"
__license__ = "MIT"
__project__ = "Open OTK (Open Ollama Toolkit)"

__all__ = [
    # Core
    "OllamaClient",
    "ModelManager",
    "ChatSession",
    # Utils
    "format_response",
    "estimate_tokens",
    "chunk_text",
    "create_prompt_template",
    # Response Handling
    "ModelResponseHandler",
    "AutoModelHandler",
    "ModelType",
    "ProcessedResponse",
    "clean_thinking_tags",
    "auto_clean_response",
    # Customization
    "CustomizableModel",
    "ModelConfig",
    "ModelPresets",
    "ModelBuilder",
    "HookType",
    "HookContext",
    # Experimentation
    "ModelExperiment",
    "ModelPlayground",
    "ABTest",
    "ExperimentResult",
    "ComparisonResult",
    # CLI
    "main",
]


def main():
    """Main entry point for the OTK CLI/GUI application"""
    import sys
    import os
    
    # Import the GUI main function from the root-level otk.py
    # We need to add the parent directory to the path to import it
    parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if parent_dir not in sys.path:
        sys.path.insert(0, parent_dir)
    
    # Import and run the GUI
    try:
        import importlib.util
        otk_gui_path = os.path.join(parent_dir, 'otk.py')
        
        if os.path.exists(otk_gui_path):
            # Load the otk.py module dynamically to avoid naming conflicts
            spec = importlib.util.spec_from_file_location("otk_gui", otk_gui_path)
            otk_gui = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(otk_gui)
            otk_gui.main()
        else:
            print("❌ OTK GUI not found!")
            print("The OTK library has been installed, but the GUI application is not available.")
            print("\nYou can still use OTK as a Python library:")
            print("  from otk import OllamaClient")
            print("  client = OllamaClient()")
            sys.exit(1)
    except Exception as e:
        print(f"❌ Error launching OTK GUI: {e}")
        print("\nYou can still use OTK as a Python library:")
        print("  from otk import OllamaClient")
        print("  client = OllamaClient()")
        sys.exit(1)
