import { Component, Inject } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { MAT_DIALOG_DATA, MatDialogRef } from '@angular/material/dialog';
import { Review, SeasonInfo } from 'src/models/review';
import { Season, Show } from 'src/models/show';
import { MatSnackBar } from '@angular/material/snack-bar';
import { ReviewService } from 'src/services/review.service';

@Component({
  selector: 'app-review-create',
  templateUrl: './review-create.component.html',
  styleUrls: ['./review-create.component.scss']
})
export class ReviewCreateComponent {
  reviewForm: FormGroup;
  constructor(
    public dialogRef: MatDialogRef<ReviewCreateComponent>,
    @Inject(MAT_DIALOG_DATA) public data: { show: Show; season: Season },
    fb: FormBuilder,
    private reviewService: ReviewService,
    private snackBar: MatSnackBar
  ) {
    this.reviewForm = fb.group({
      review: ['', Validators.required],
      rating: ['', Validators.required],
      seasonInfo: fb.group({
        showId: data.show.id,
        seasonNumber: data.season.seasonNumber
      })
    });
  }

  /**
   * Closes the dialog
   */
  public close(): void {
    this.dialogRef.close();
  }

  /**
   * Submits the review
   */
  public submit(): void {
    const newReview = new Review(
      undefined,
      undefined,
      new SeasonInfo(this.data.show.id, undefined, this.data.season.seasonNumber, undefined),
      this.reviewForm.get('review')!.value,
      this.reviewForm.get('rating')!.value
    );
    this.reviewService.create(newReview).subscribe(() => {
      this.snackBar.open('Review successfully created', '', { duration: 3000 });
      this.close();
    });
  }
}
