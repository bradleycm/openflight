import asyncio
import signal
import os

def main():
  from openflight_video.src.streaming import OpenFlightVideoStream

  video_stream = OpenFlightVideoStream()
  video_stream.set_input_device(0)  # Use default camera device
  video_stream.set_resolution((640, 480))  # Set video resolution to 640x480
  video_stream.set_frame_rate(30)  # Set frame rate to 30 fps
  video_stream.set_encoding_format('h264')  # Use H.264 encoding format

  # Define signal handler for clean shutdown
  async def handle_signal():
    signal_received = False
    for signame in {'SIGINT', 'SIGTERM'}:
      asyncio.get_event_loop().add_signal_handler(getattr(signal, signame), lambda: asyncio.create_task(shutdown()))
    while not signal_received:
      await asyncio.sleep(1)

  async def shutdown():
    video_stream.stop()
    tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
    [task.cancel() for task in tasks]
    await asyncio.gather(*tasks)

  print('Starting OpenFlight Software...')
  print('Starting OpenFlight Video stream...')

  try:
    output_path = os.path.join(os.getcwd(), 'video.avi')  
    video_stream.start(output_path)
    asyncio.run(handle_signal())
  except Exception as e:
    print(f'Error: {e}')


if __name__ == "__main__":
  main()