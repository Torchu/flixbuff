import { Exclude, Expose, Type } from 'class-transformer';

export class ReviewerInfo {
  /**
   * ID of the reviewer
   * @type{string}
   */
  @Expose({ name: 'reviewer_id' })
  @Exclude({ toPlainOnly: true })
    reviewerId: string;

  /**
   * Username of the reviewer
   * @type{string}
   */
  @Expose({ name: 'reviewer_username' })
  @Exclude({ toPlainOnly: true })
    reviewerUsername: string;

  constructor(reviewerId?: string, reviewerUsername?: string) {
    this.reviewerId = reviewerId ? reviewerId : '';
    this.reviewerUsername = reviewerUsername ? reviewerUsername : '';
  }
}

export class SeasonInfo {
  /**
   * ID of the show
   * @type {number}
   */
  @Expose({ name: 'show_id' })
    showId: number;

  /**
   * Name of the show
   */
  @Expose({ name: 'show_name' })
  @Exclude({ toPlainOnly: true })
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
  @Exclude({ toPlainOnly: true })
    seasonName: string;

  /**
   * Poster of the season
   * @type {string}
   */
  @Expose({ name: 'season_poster' })
  @Exclude({ toPlainOnly: true })
    seasonPoster: string;

  /**
   * Constructor
   */
  constructor(showId?: number, showName?: string, seasonNumber?: number, seasonName?: string, seasonPoster?: string) {
    this.showId = showId ? showId : 0;
    this.showName = showName ? showName : '';
    this.seasonNumber = seasonNumber ? seasonNumber : 0;
    this.seasonName = seasonName ? seasonName : '';
    this.seasonPoster = seasonPoster ? seasonPoster : '';
  }

  /**
   * Returns the image URL for the season's poster.
   */
  getPosterUrl(): string {
    return this.seasonPoster != 'None'
      ? `https://image.tmdb.org/t/p/original${this.seasonPoster}`
      : 'https://via.placeholder.com/500x750';
  }
}

export class Review {
  /**
   * The id of the review
   * @type {string}
   */
  @Expose({ name: '_id' })
  @Exclude({ toPlainOnly: true })
    id: string;

  /**
   * The id of the reviewer user
   * @type {string}
   */
  @Expose({ name: 'reviewer_info' })
  @Exclude({ toPlainOnly: true })
  @Type(() => ReviewerInfo)
    reviewerInfo: ReviewerInfo;

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
  constructor(id?: string, reviewerInfo?: ReviewerInfo, seasonInfo?: SeasonInfo, review?: string, rating?: number) {
    this.id = id ? id : '';
    this.reviewerInfo = reviewerInfo ? reviewerInfo : new ReviewerInfo();
    this.seasonInfo = seasonInfo ? seasonInfo : new SeasonInfo();
    this.review = review ? review : '';
    this.rating = rating ? rating : 0;
  }
}

export class ReviewList {
  @Type(() => Review)
    items: Array<Review>;

  @Expose()
    total: number;

  constructor(items: Array<Review>, total: number) {
    this.items = items;
    this.total = total;
  }
}
