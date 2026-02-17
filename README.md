[![Build Status](https://github.com/siddhuwarrier/curriculum-vitae/actions/workflows/ci.yml/badge.svg)](https://github.com/siddhuwarrier/curriculum-vitae/actions/workflows/ci.yml)

**Download a PDF copy of my most up-to-date CV** from the [Releases Page](https://github.com/siddhuwarrier/curriculum-vitae/releases/latest).

# LaTeX Curriculum Vitae

My CV built with LaTeX, featuring automated PDF generation and deployment via GitHub Actions.

## What this includes

- **LaTeX Source**: Modular `.tex` source code. Each section is its own file.
- **Makefile**: Simple local build system (`make clean all`).
- **CI/CD**: GitHub Actions automatically:
  - Compiles the LaTeX source into a PDF on every push to `main`.
  - Increments the version tag (e.g., `v1`, `v2`).
  - Creates a new [GitHub Release](https://github.com/siddhuwarrier/curriculum-vitae/releases) with the PDF attached.

## Local Usage

### Prerequisites

You need a LaTeX distribution ([like TeX Live or MiKTeX](https://www.latex-project.org/get/)).

### Build

To generate the PDF locally:

```bash
make all
```

### Clean

To remove auxiliary build files:
`make clean`

## Forking this Repo

Feel free to fork this repository to build your own CV!

1. **Modify**: Edit `cv.tex` with your own details.
2. **Push**: Push your changes to the `main` branch.
3. **Download**: Check the **Releases** tab in your repository for the compiled PDF.

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
