"""Copy selected Agent Skills into a harness's project or user skills directory."""

import argparse
from pathlib import Path
import shutil


SKILLS = Path(__file__).resolve().parent / 'skills'
DEPENDENCIES = {
    'documenting-with-sources': {'writing-quotation'},
    'paper-details': {'documenting-with-sources', 'writing-quotation'},
    'survey': {'documenting-with-sources', 'writing-quotation'},
}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('names', metavar='SKILL', nargs='*', help='copy only these skills; defaults to all')
    parser.add_argument('--dest', type=Path, help='skills directory used by the harness')
    parser.add_argument('--list', action='store_true', help='list bundled skills')
    parser.add_argument('--dry-run', action='store_true', help='show what would be copied')
    args = parser.parse_args()
    available = {p.name for p in SKILLS.iterdir() if (p / 'SKILL.md').is_file()}
    if args.list:
        print('\n'.join(sorted(available)))
        return
    if not args.dest:
        parser.error('--dest is required when installing')
    requested = set(args.names) or available
    unknown = requested - available
    if unknown:
        parser.error('unknown skill: ' + ', '.join(sorted(unknown)))
    selected = requested | set().union(*(DEPENDENCIES.get(name, set()) for name in requested))
    destination = args.dest.expanduser().resolve()
    collisions = [name for name in sorted(selected) if (destination / name).exists() or (destination / name).is_symlink()]
    if collisions:
        parser.error('existing folders were kept: ' + ', '.join(collisions))
    for name in sorted(selected):
        target = destination / name
        if not args.dry_run:
            shutil.copytree(SKILLS / name, target)
        print(f'{"Would copy" if args.dry_run else "Installed"}: {target}')


if __name__ == '__main__':
    main()
