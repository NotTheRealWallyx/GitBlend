import git
from gitblend.commands import delete_tag, create_tag
from copy import deepcopy


def run(args):
    old_tag = args.old_tag
    new_tag = args.new_tag

    try:
        print(f"🔄 Renaming tag '{old_tag}' to '{new_tag}'...")
        delete_tag.run(args)

        new_args = deepcopy(args)
        new_args.tag = new_tag

        create_tag.run(new_args)

        print(f"✅ Tag '{old_tag}' has been renamed to '{new_tag}' successfully.")
    except Exception as e:
        print(f"❌ Error while renaming tag '{old_tag}' to '{new_tag}': {e}")
        sys.exit(1)
