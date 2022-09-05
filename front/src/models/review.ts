import { Exclude, Expose, Type } from 'class-transformer';

export class SeasonInfo {
  /**
   * ID of the show
   * @type {number}
   */
  @Expose({ name: 'show_id' })
    showId: string;

  /**
   * Name of the show
   */
  @Expose({ name: 'show_name' })
  @Exclude({ toClassOnly: true })
    showName: string;

  /**
   * Number of the season
   * @type {number}
   */
  @Expose({ name: 'season_number' })
    seasonNumber: number;

  /**
   * Name of the season
   * @type {string}
   */
  @Expose({ name: 'season_name' })
  @Exclude({ toClassOnly: true })
    seasonName: string;

  /**
   * Constructor
   */
  constructor(showId: string, showName: string, seasonNumber: number, seasonName: string) {
    this.showId = showId;
    this.showName = showName;
    this.seasonNumber = seasonNumber;
    this.seasonName = seasonName;
  }
}

export class Review {
  /**
   * The id of the review
   * @type {string}
   */
  @Expose({ name: '_id' })
  @Exclude({ toClassOnly: true })
    id: string;

  /**
   * The id of the reviewer user
   * @type {string}
   */
  @Expose()
  @Exclude({ toClassOnly: true })
    reviewer: string;

  /**
   * Info about the season
   * @type {SeasonInfo}
   */
  @Expose({ name: 'season_info' })
  @Type(() => SeasonInfo)
    seasonInfo: SeasonInfo;

  /**
   * The review text
   * @type {string}
   */
  @Expose() review: string;

  /**
   * The review rating
   * @type {number}
   */
  @Expose() rating: number;

  /**
   * Constructor
   */
  constructor(id: string, reviewer: string, seasonInfo: SeasonInfo, review: string, rating: number) {
    this.id = id;
    this.reviewer = reviewer;
    this.seasonInfo = seasonInfo;
    this.review = review;
    this.rating = rating;
  }
}
