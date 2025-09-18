import os
import ast

PATENTABLE_KEYWORDS = [
    "algorithm", "protocol", "architecture", "unique", "novel",
    "process", "optimization", "ai", "ml", "machine learning", "cryptography",
    "data structure", "compression", "security", "invention", "patent"
]

def is_patentable(node):
    name = getattr(node, 'name', '').lower()
    doc = ast.get_docstring(node) or ""
    doc = doc.lower()
    if any(k in name for k in PATENTABLE_KEYWORDS) or any(k in doc for k in PATENTABLE_KEYWORDS):
        return True
    return False

def analyze_file(file_path):
    results = []
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source = f.read()
        tree = ast.parse(source, filename=file_path)
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.ClassDef)):
                component = f"{os.path.basename(file_path)}:{node.name}"
                if is_patentable(node):
                    results.append({"component": component, "status": "Potentially Patentable"})
                else:
                    results.append({"component": component, "status": "Non-Patentable"})
    except Exception as e:
        results.append({"component": os.path.basename(file_path), "status": f"Error: {str(e)}"})
    return results

def analyze_repo(repo_path):
    all_results = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                file_results = analyze_file(file_path)
                all_results.extend(file_results)
    return all_results