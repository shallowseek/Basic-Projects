import json



def list_all_youtube_videos(videos):
    enumerate_videos = enumerate(videos, start=1) # this will start the index from 1 and since we are using enumerate function, it will return an enumerate object with index and value.
    # this will return an enumerate object with index and value as (index, videos) where index is the numbers and each video is a dictionary. and therefore only key would be joined with index to form a tuple and value as a dictionary.
    # i have made json as list of dictionaries where each dictionary is a video and each video has title, duration, and description.
    # so enumerate will return an object with index and value as (index, videos) where (index=1, videos={title: "video1", duration: "10:00", description: "description of video1"})
    
    print(enumerate_videos) # this will print the enumerate object.
    print('*' * 70) # this will print the line of * to separate the output.
    for index,video in enumerate_videos: # this will unpack the enumerate object into index and value.
         # since videos 
         print(f"{index}--{video['title']}--{video['duration']}") # this will print the index and the title of the video.
         print('*' * 70) # this will print the line of * to separate the output.





def add_video(videos):
    name = input("Enter the name of the video: ").lower().strip() # this will take the input from the user and convert it to lower case.
    duration = input("Enter the duration of the video: ") # this will take the input from the user and convert it to integer.
    description = input("Enter the description of the video: ").lower().strip() # this will take the input from the user and convert it to lower case.
    video = {
        "title": name,
        "duration": duration,
        "description": description
    }
    videos.append(video) # this will append the video to the list of videos.
    save_data(videos) # this will save the data to the file.
# this is a function to add a new video to the list of videos.




def update_video(videos):
    list_all_youtube_videos(videos) # this will list all the videos before updating.
    name = input("Enter the name of the video: ").lower().strip()
    found = False  # Track whether any video matched

    for video in videos:
        if video["title"] == name:
            update = input("What do you want to update? (title, duration, description): ").lower().strip()
            new = input("Enter the new value: ").lower().strip()

            if update in video:# will check for keys
                video[update] = new
                print("Video updated successfully.")
            else:
                print("Invalid field to update.")
            found = True
            break  # Exit after updating the video

    if not found:# will reverse the condition if video is not found.
        print("Video not found")

    

    #after updating the video, we need to save the data to the file and by again converting it back to json string otherwise chnages won't be seen on main file.
    save_data(videos) # this will save the data to the file.
# this is a function to update the video details.



def load_data():
    try:
        with open("youtube_videos.json", "r") as file:
            videos = json.load(file)# will return either dictionary or list.
            print(videos)
            return videos
    except FileNotFoundError:# there are many types of exceptions. we can use FileNotFoundError to check if the file is not found.
        print("File not found. Creating a new file.")
        with open("youtube_videos.json", "w") as file:
            json.dump([], file)
        return []
    


def delete_video(videos):
    list_all_youtube_videos(videos)
    index = int(input("Enter the index of the video to delete: ")) - 1 # this will take the input from the user and convert it to integer.
    if 1 <= index < len(videos): # this will check if the index is valid or not.
        videos.pop(index-1) # this will remove the video from the list of videos sinnce we are using 0 based index in list.
        
        print("Video deleted successfully.")
    else:
        print("Invalid index. Video not deleted.")
    # after deleting the video, we need to save the data to the file and by again converting it back to json string otherwise chnages won't be seen on main file.
    save_data(videos) # this will save the data to the file.
# this is a function to delete the video from the list of videos.


def save_data(videos):# this is a helper function to save the data to the file since in every function we need to save the data to the file.hence we are using this function.
    with open("youtube_videos.json", "w") as file:
        json.dump(videos, file)
    





def main():    # This is the main function that will be called when the script is run.
    # videos = [] # This is an empty list that will be used to store the youtube videos where each video will be a dictionary.
    videos = load_data() # This will load the data from the file and return a list of videos.
    
    
    while True:
        print("\n Youtube Manager")
        print("1. List all youtube videos")
        print("2. Add a new youtube video")
        print("3. Update a youtube video details")
        print("4. Delete a youtube video")
        print("5.Exit the application")
        choice = input("Enter your choice:")
        # if choice == '1':
        #     print("Listing all youtube videos")
        #     # Call the function to list all youtube videos
        # elif choice == '2':
        #     print("Adding a new youtube video")
        #     # Call the function to add a new youtube video
        # elif choice == '3':
        #     print("Updating a youtube video details")
        #     # Call the function to update a youtube video details
        # elif choice == '4':
        #     print("Deleting a youtube video")
        #     # Call the function to delete a youtube video
        # elif choice == '5':
        #     print("Exiting the application")
        #     break
        # else:
        #     print("Invalid choice. Please try again.")
        match choice:
            case '1':
                print("Listing all youtube videos")
                list_all_youtube_videos(videos) # call the function to list all youtube videos
                # we need to call api to get the list of videos.
                # Call the function to list all youtube videos
            case '2':

                print("Adding a new youtube video")
                add_video(videos) # Call the function to add a new youtube video
                # Call the function to add a new youtube video
            case '3':
                print("Updating a youtube video details")
                update_video(videos) # Call the function to update a youtube video details
                # Call the function to update a youtube video details
            case '4':
                print("Deleting a youtube video")
                delete_video(videos) # Call the function to delete a youtube video
                # Call the function to delete a youtube video
            case '5':
                print("Exiting the application")
                break
            case _:# underscore all rest cases.
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main() # This will call the main function when the script is run.


#new sytnas for update videos function
# You need to loop through the list and check if any video's title matches the input string:

# for video in videos:
#     if video["title"] == name:
#         # do something

# Or, if you just want to check if a video exists with that title:

# found = any(video["title"] == name for video in videos)
# if found:
#     print("Video found")
# else:
#     print("Not found")
