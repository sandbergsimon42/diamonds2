import { ApiModelProperty } from "@nestjs/swagger";
import { PositionDto } from "./position.dto";
import {
  IsEmail,
  IsString,
  Min,
  Max,
  MinLength,
  MaxLength,
} from "class-validator";
export class BotRegistrationDto {
  @ApiModelProperty({
    description:
      "A valid email address for this bot. Will be used for communication. Will for example be used if you are one of the winners.",
  })
  @IsEmail()
  readonly email: string;

  @ApiModelProperty({
    description: "The name you want to use for the bot.",
  })
  @IsString()
  @MinLength(1)
  @MaxLength(10)
  readonly botName: string;
}
