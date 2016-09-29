import argparse, os, re
#Python does not support repeated groups so we'll split it later
tags_line_pattern = re.compile(r"^\/\/tags .+")
tags_pattern = re.compile(r"@[\w\d]+")
def parseArgs():
    parser = argparse.ArgumentParser(description="Parse Tags and Create Report")
    parser.add_argument('--tags', help='Do not include spaces. ex: GT,smoke', type=str, required=True)
    parser.add_argument('--srcDir', help='Path to where files to parse are. Put in quotes', type=str, required=True)
    parser.add_argument('--outDir', help='Where to store csv file (optional -- csv will not be created if not provided)', type=str)
    return parser.parse_args()

def findTags(srcDir, tags):
    print('srcDir', srcDir)
    tagInfo = {}
    for tag in tags.split(","):
        tagInfo[tag.strip()] = {
            'included_in':[]
        };
    for root, directories, files in os.walk(srcDir):
        # print(root)
        # print(directories)
        # print(files)
        for fl in files:
            tag_string = findTagString(os.path.join(root, fl))
            continue
        continue

    print(tagInfo)
    return tagInfo

def findTagString(filePath):
    with open(filePath, 'r') as f:
        contents = f.read()
        matches = tags_line_pattern.search(contents)
        print('searched file', filePath)
        print('all matched', matches.group())
        tag_matches = tags_pattern.findall(matches.group())
        print('tag_matches', tag_matches)

if __name__ == "__main__":
    args = parseArgs()
    tag_info = findTags(args.srcDir, args.tags)
