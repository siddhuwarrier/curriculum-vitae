[![Build Status](https://github.com/siddhuwarrier/curriculum-vitae/actions/workflows/ci.yml/badge.svg)](https://github.com/siddhuwarrier/curriculum-vitae/actions/workflows/ci.yml)

**Download a PDF copy of my most up-to-date CV** from the [Releases Page](https://github.com/siddhuwarrier/curriculum-vitae/releases/latest).

# Curriculum Vitae

My CV built with LaTeX, featuring automated PDF generation and deployment via GitHub Actions.

## What this includes

- **LaTeX Source**: Modular `.tex` source code. Each section is its own file.
- **Makefile**: Simple local build system (`make clean all`).
- **CI/CD**: GitHub Actions automatically:
  - Compiles the LaTeX source into a PDF on every push to `main`.
  - Uploads the PDF to Cloudflare R2 at `siddhuw.assets/cv.pdf`.
  - Increments the version tag (e.g., `v1`, `v2`).
  - Creates a new [GitHub Release](https://github.com/siddhuwarrier/curriculum-vitae/releases) with the PDF attached.

## Cloudflare R2 Deployment Setup

Add this repository secret before running CI:

- `CLOUDFLARE_API_TOKEN`: token with permission to read your Cloudflare account and write objects to R2.
- `CLOUDFLARE_ACCOUNT_ID`: your Cloudflare account id for the target bucket.

The workflow uploads `cv.pdf` as `siddhu_warrier_cv.pdf` to bucket `siddhuw-info` on every successful build via `tools/ci/upload_cv_to_cloudflare.py`.
To make it publicly downloadable, enable public access for the bucket (R2.dev or custom domain).

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
