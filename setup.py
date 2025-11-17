from setuptools import setup, find_packages


setup(name='OpenVoice',
      version='0.1.0',
      description='Instant voice cloning by MyShell - Enhanced by Gedeon.',
      long_description=open('README.md').read().strip(),
      long_description_content_type='text/markdown',
      keywords=[
            'text-to-speech',
            'tts',
            'voice-clone',
            'zero-shot-tts'
      ],
      url='https://github.com/beethogedeon/OpenVoice',
      project_urls={
        'Documentation': 'https://github.com/beethogedeon/OpenVoice/blob/main/docs/USAGE.md',
        'Changes': 'https://github.com/beethogedeon/OpenVoice/releases',
        'Code': 'https://github.com/beethogedeon/OpenVoice',
        'Issue tracker': 'https://github.com/beethogedeon/OpenVoice/issues',
      },
      author=['MyShell, Gedeon GBEDONOU'],
      author_email=['ethan@myshell.ai','beethovengedeon@gmail.com'],
      license='MIT License',
      packages=find_packages(),

      python_requires='>=3.9',
      install_requires=[
            'librosa==0.11.0',
'git+https://github.com/SYSTRAN/faster-whisper',
'pydub==0.25.1',
'wavmark',
'numpy',
'eng_to_ipa',
'inflect',
'unidecode',
'whisper-timestamped',
'openai',
'python-dotenv',
'pypinyin',
'cn2an',
'jieba',
'gradio',
'langid'
      ],
      zip_safe=False
      )

