import argparse

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class JobArgs:
    source_id: str
    full_load: bool
    job_id: str
    output_dir: Path
    retries: int


def main() -> None:

    parser = argparse.ArgumentParser(
        prog="run_job.py",
        description="Run extraction pipeline."
        )

    parser.add_argument("--source-id", choices=["csv", "parquet", "sftp"], required=True, help="Metadata key for source extraction.") # Required argument
    parser.add_argument("--full-load", action="store_true", help="Specifies if full load will be executed.") # Boolean argument
    parser.add_argument("--job-id", required=True, help="Job ID for metadata retrieval.")
    parser.add_argument("--output-dir", default=".", help="Where output is being written.")

    parser.add_argument("--retries", type=int, default=3)#


    args = parser.parse_args()
    print("Parsed arguments:")
    print(f"  job_id = {args.job_id}")
    print(f"  source_id = {args.source_id}")
    print(f"  retries = {args.retries, type(args.retries)}")

    job_args = JobArgs(
        source_id=args.source_id,
        full_load=args.full_load,
        job_id=args.job_id,
        output_dir=Path(args.output_dir),
        retries=args.retries
    )

    print(job_args)


if __name__ == "__main__":
    main()
