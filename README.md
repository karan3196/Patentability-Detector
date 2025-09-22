# Patentability Detector

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[Repository Link](https://github.com/karan3196/Patentability-Detector)

## Overview

**Patentability Detector** is a tool designed to analyze the codebase of any given GitHub repository to identify components that may be patentable. It distinguishes between novel algorithms, unique processes, architectures (potentially patentable), and parts like UI code or boilerplate (likely not patentable).

---

## Features

- **Repository Analysis:** Input any GitHub repository URL for analysis.
- **Component Classification:**
  - **Patentable:** Detects unique algorithms, novel processes, and architectural innovations.
  - **Not Patentable:** Flags standard implementations, UI code, and boilerplate.
- **TypeScript Based:** The project is implemented in TypeScript for strong typing and maintainability.
- **Easy Integration:** Designed to be integrable as a CLI tool or service.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture and Components](#architecture-and-components)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Architecture and Components

### Main Components

1. **Repository Analyzer:**  
   - Fetches and parses the remote GitHub repository.
   - Scans files for patterns and structures indicating novelty.

2. **Patentability Classifier:**  
   - Uses heuristics to separate potentially patentable components from non-patentable ones.
   - Focuses on algorithms, data flows, and architectural decisions.

3. **Result Renderer:**  
   - Outputs a detailed report categorizing files and code fragments.

### Technologies Used

- **TypeScript:** Primary language for static typing and code reliability.
- **Node.js:** Execution environment.
- **GitHub API:** For fetching repository contents and metadata.
- **Custom Heuristics:** Rule-based logic for detection.

---

## Installation

### Prerequisites

- Node.js (v16+ recommended)
- npm (Node Package Manager)

### Steps

```bash
git clone https://github.com/karan3196/Patentability-Detector.git
cd Patentability-Detector
npm install
```

---

## Usage

### Analyzing a Repository

1. **Command Line:**

   ```bash
   npm start -- --repo https://github.com/example/repo
   ```

2. **Programmatic Usage:**

   ```typescript
   import { analyzeRepo } from 'patentability-detector';

   analyzeRepo('https://github.com/example/repo')
     .then(report => {
       console.log(report);
     });
   ```

### Output

The tool will display:
- **Patentable Components:** List of files/sections with innovative algorithms/processes/architectures.
- **Non-Patentable Components:** UI files, boilerplate, standard implementations.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.  
Feel free to open issues for feature requests or bug reports.

---

## License

This project is licensed under the [Apache License 2.0](LICENSE).

---

## Contact

Maintainer: [karan3196](https://github.com/karan3196)

For questions or suggestions, please open a [GitHub Issue](https://github.com/karan3196/Patentability-Detector/issues).