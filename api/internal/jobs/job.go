package jobs

type Job struct {
	ID             string `json:"id"`
	Status         string `json:"status"`
	CreatedAt      string `json:"created_at"`
	UpdatedAt      string `json:"updated_at"`
	InputVideoPath string `json:"input_video_path"`
	ConfigPath     string `json:"config_path"`
	RunDir         string `json:"run_dir"`
	Error          string `json:"error,omitempty"`
}
