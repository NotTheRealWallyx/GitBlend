import git
from gitblend.commands import delete_tag, create_tag


def run(args):
    old_tag = args.old_tag
    new_tag = args.new_tag

    try:
        delete_tag.run(args)

        args.tag = new_tag
        create_tag.run(args)

        print(f"✅ Tag '{old_tag}' has been renamed to '{new_tag}' successfully.")
    except Exception as e:
        print(f"Error: {e}")
