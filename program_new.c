
typedef struct changedPixel{
	 char r;
	 char b;
	 char g;
	 short addr;
}changedPixel;

const int endOfFramePixelIndex[189] = {2100, 2940, 3780, 4620, 5460, 6300, 7140, 7980, 9240, 10500, 11760, 13020, 14280, 15540, 16800, 18900, 21000, 23100, 25200, 27300, 29400, 31500, 31500, 31500, 31550, 31600, 31650, 31700, 31750, 31800, 31850, 31900, 31950, 32000, 32050, 32100, 32150, 32200, 32250, 32300, 32350, 32400, 32450, 32500, 32550, 32600, 32650, 32700, 32750, 32800, 32850, 32900, 32950, 33000, 33050, 33100, 33150, 33200, 33250, 33300, 33350, 33400, 33450, 33500, 33550, 33590, 33616, 33619, 33632, 33655, 33686, 33725, 33772, 33825, 33884, 33954, 34035, 34123, 34219, 34334, 34461, 34607, 34771, 34950, 35145, 35361, 35599, 35855, 36128, 36409, 36714, 37026, 37349, 37677, 38004, 38327, 38656, 38990, 39328, 39676, 40033, 40401, 40768, 41136, 41506, 41863, 42226, 42568, 42892, 43190, 43457, 43697, 43929, 44142, 44350, 44546, 44719, 44895, 45060, 45210, 45362, 45503, 45642, 45763, 45873, 45969, 46043, 46104, 46156, 46197, 46233, 46264, 46291, 46311, 46331, 46350, 46364, 46375, 46386, 46394, 46399, 46403, 46407, 46857, 47288, 47729, 48168, 48610, 49059, 49492, 49929, 50372, 50815, 51263, 51705, 52138, 52582, 53021, 53465, 54025, 54749, 55707, 56802, 57572, 58274, 58898, 59643, 60486, 61337, 62151, 62848, 63614, 64495, 65362, 66197, 67050, 67943, 68898, 69872, 70778, 71617, 72365, 72972, 73351, 73575, 73684, 73716, 73731, 73745};
const int totalCount = 73745;
const char included_animations[4][11] = {"bavaria", "fur", "color_shift", "explosion"};
const int animation_name_length[4] = {7, 3, 11, 9};
const int animation_end_pixels[] = {33590, 46407, 53465, 73745};
int digled_ctr = 12; // 1 init_strip + 11 LUTs for proper white color

int AnimationFrameDelay(short i)
{
	short animation_length_index = animation_name_length[i];
	char current_animation[animation_length_index];
	strcpy(current_animation, included_animations[i]);
	int animation_delay_time = 400000;

	if(strcmp(current_animation, "anime_fight") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "bavaria") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "birds") == 0)
	{
		animation_delay_time = 400000;
	}
	else if(strcmp(current_animation, "color_shift") == 0)
	{
		animation_delay_time = 650000;
	}
	else if(strcmp(current_animation, "dove") == 0)
	{
		animation_delay_time = 300000;
	}
	else if(strcmp(current_animation, "ellipse") == 0)
	{
		animation_delay_time = 450000;
	}
	else if(strcmp(current_animation, "explosion") == 0)
	{
		animation_delay_time = 250000;
	}
	else if(strcmp(current_animation, "faded_rainbow") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "flames") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "fur") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "hexagons") == 0)
	{
		animation_delay_time = 650000;
	}
	else if(strcmp(current_animation, "infinity") == 0)
	{
		animation_delay_time = 350000;
	}
	else if(strcmp(current_animation, "inova_logo") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "inova_logo_prep") == 0)
	{
		animation_delay_time = 500000;
	}
	else if(strcmp(current_animation, "newyear") == 0)
	{
		animation_delay_time = 400000;
	}
	else if(strcmp(current_animation, "pokemon") == 0)
	{
		animation_delay_time = 600000;
	}
	else if(strcmp(current_animation, "rainbow_wave") == 0)
	{
		animation_delay_time = 350000;
	}
	else if(strcmp(current_animation, "spiral_fullscreen") == 0)
	{
		animation_delay_time = 350000;
	}
	else
	{
		animation_delay_time = 400000;
	}

	return animation_delay_time;
}

void wait(int d)
{
	delay(d);
	iseled_reset_counter++;
	if (iseled_reset_counter == 10000)
		iseled_reset();
}

void setPixel(int r, int g, int b, int addr)
{
	if(digled_ctr == 8402) // refresh the NXP MCU counter before it reaches 10k
	{
		digLED_Init_Interface(NUMBER_OF_INTERFACES, iseled1_InitConfig);
		delay(10000);
		digLED_Init_Strip(&testInitType, &digLEDResultStrip1, strip);
		delay(10000);
		digled_ctr = 2;
	}
	Set_RGB_Params.Red = r;
	Set_RGB_Params.Green = g;
	Set_RGB_Params.Blue = b;
	digLED_Set_RGB(Set_RGB_Params.Red, Set_RGB_Params.Green, Set_RGB_Params.Blue, addr, strip);
	digled_ctr = 2;
	wait(1000);
}

void led_matrix()
{
	int nextEndFrame = endOfFramePixelIndex[0];
	short frameIndex = 0;
	short animationIndex = 0;
	int delay_time = AnimationFrameDelay(0);
	int frame_count_adjust = 0;//in case there is a loop, this will reduce the number of for loop iterations

	//change these 3 values depending on the loop you'd like to have
	int loop_start_point = 33591;
	int loop_end_point = 53465;
	short loop_count = 3;

	//these two are set to zero initially
	short loop_start_index = 0;
	short loop_end_index = 0;
	short start_animation_index = 0;
	short end_animation_index = 0;

	if(loop_count != 0)//to locate the start and end of the loop in frame and animation arrays
	{
		for(int t = 0; t < 189; t++)
		{
			if(endOfFramePixelIndex[t] == loop_start_point - 1)
			{
				loop_start_index = t;
			}
			else if(endOfFramePixelIndex[t] == loop_end_point)
			{
				loop_end_index = t;
				break;
			}
			else
				continue;

		}

		for(int z = 0; z < 4; z++)
		{
			if(animation_end_pixels[z] == loop_start_point - 1)
			{
				start_animation_index = z;
			}
			else if(loop_end_point == animation_end_pixels[z])
			{
				end_animation_index = z;
				break;
			}
			else
				continue;
		}
		frame_count_adjust = loop_end_point - loop_start_point + 1;
	}
	else
		frame_count_adjust = 0;

	for(int i = 0; i < totalCount - frame_count_adjust; i++)
	{
		if(loop_start_point > endOfFramePixelIndex[i] + 1)//before the loop starts
		{
			delay_time = AnimationFrameDelay(animationIndex);
			if(i == nextEndFrame)
			{
				frameIndex += 1;
				nextEndFrame = endOfFramePixelIndex[frameIndex];
				if(endOfFramePixelIndex[i] == animation_end_pixels[animationIndex])
				{
					wait(10000000);
					animationIndex++;
				}
				else
				{
					wait(delay_time);
				}
			}
			setPixel((int)changedPixels[i].r, (int)changedPixels[i].g, (int)changedPixels[i].b, changedPixels[i].addr);
		}
		else if(endOfFramePixelIndex[i] == loop_start_point - 1) // loop starts
		{
			while(loop_count > 0)
			{
				for(int j = loop_start_point - 1; j < loop_end_point; j++)//-1 is due to indexing of arrays
				{
					setPixel((int)changedPixels[j].r, (int)changedPixels[j].g, (int)changedPixels[j].b, changedPixels[j].addr);
				    for(int k = 0; k < 189; k++)
					{
						if(endOfFramePixelIndex[k] == j)//end of frame in loop
						{
							wait(250000);
						}
					}
				}

				if(loop_count == 1)
				{
					loop_start_point = -1;
					frameIndex = frameIndex + loop_end_index - loop_start_index;
					animationIndex = animationIndex + end_animation_index - start_animation_index;
				}
				else
				{
					for(int c = 0; c < 2100; c++)//to clean the screen when the loop repeats itself
					{
						setPixel(0, 0, 0, c);
					}
				}

				loop_count--;
			}
		}
		else//the part after the loop
		{
			delay_time = AnimationFrameDelay(animationIndex);
			if(i == nextEndFrame)
			{
				frameIndex += 1;
				nextEndFrame = endOfFramePixelIndex[frameIndex];
				if(endOfFramePixelIndex[i + frame_count_adjust] == animation_end_pixels[animationIndex])
				{
					wait(10000000);
					animationIndex++;
				}
				else
				{
					wait(delay_time);
				}
			}
			setPixel((int)changedPixels[i + frame_count_adjust].r, (int)changedPixels[i + frame_count_adjust].g, (int)changedPixels[i + frame_count_adjust].b, changedPixels[i + frame_count_adjust].addr);
		}
	}
	wait(50000000);
}